import os
import argparse
import pandas as pd
import torch
from datetime import timedelta
import whisper
import re
import numpy as np
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import subprocess
import tempfile
import uuid


# ==============================
# 1. Speech-to-Text (STT) Module
# ==============================


def download_audio_from_youtube(youtube_url, output_format="wav"):
    """
    Downloads audio from a YouTube video using yt-dlp.
    Returns the path to the downloaded audio file.
    """
    unique_name = f"temp_{uuid.uuid4().hex[:8]}.{output_format}"
    output_path = os.path.join(tempfile.gettempdir(), unique_name)

    command = [
        "yt-dlp",
        "-x", "--audio-format", output_format,
        "--output", output_path,
        youtube_url
    ]
    subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return output_path


def get_audio_duration(audio_path):
    """
    Uses ffprobe to get the duration of the audio file in seconds.
    Ensure that ffmpeg/ffprobe is installed and accessible in your PATH.
    """
    result = subprocess.run(
        [
            "ffprobe", "-v", "error", "-show_entries",
            "format=duration", "-of",
            "default=noprint_wrappers=1:nokey=1", audio_path
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT
    )
    return float(result.stdout)

def transcribe_audio(audio_path, device="cpu"):
    model = whisper.load_model("large-v2", device=device)
    # Change language as needed; currently set to "ar" (Arabic)
    result = model.transcribe(audio_path, language="ar")
    full_text = result["text"]
    sentences = re.split(r'(?<=[\.!\؟])\s+', full_text.strip())
    sentences = [s.strip() for s in sentences if s.strip()]
    
    # Use the result's duration if available; otherwise, get it using ffprobe.
    total_duration = result.get("duration")
    if total_duration is None:
        total_duration = get_audio_duration(audio_path)
    
    num_sentences = len(sentences)
    if num_sentences == 0:
        return []
    interval = total_duration / num_sentences
    stt_results = []
    for idx, sentence in enumerate(sentences):
        start_sec = idx * interval
        end_sec = (idx + 1) * interval
        start_time = str(timedelta(seconds=int(start_sec))) + f",{int((start_sec % 1) * 1000):03d}"
        end_time = str(timedelta(seconds=int(end_sec))) + f",{int((end_sec % 1) * 1000):03d}"
        stt_results.append({
            "Start Time": start_time,
            "End Time": end_time,
            "Sentence": sentence
        })
    return stt_results


# ==============================
# 2. Translation Module (Bypassed)
# ==============================
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Load these once globally so they're not re-loaded on every call.
MODEL_PATH = r"c:\Year 2\Y2- Block C\Complete_pipeline\models\translation_model\final_model"
tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_PATH)
# Optionally, move model to CUDA if available.
device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)
model.eval()

def translate_sentences(sentences, device=device, batch_size=8):
    """
    Translates a list of sentences using a locally saved translation model.
    This version uses batch processing for improved performance.
    """
    translations = []
    
    # Process the sentences in batches.
    for i in range(0, len(sentences), batch_size):
        batch = sentences[i:i+batch_size]
        # Batch tokenization
        inputs = tokenizer(batch, return_tensors="pt", padding=True, truncation=True, max_length=128)
        inputs = {k: v.to(device) for k, v in inputs.items()}
        
        # Generate translations for the batch
        outputs = model.generate(**inputs, max_length=128, num_beams=5)
        
        # Decode all outputs
        batch_translations = tokenizer.batch_decode(outputs, skip_special_tokens=True)
        translations.extend(batch_translations)
    
    return translations



# ==============================
# 3. Emotion Classification Module
# ==============================
class EmotionClassifier:
    """
    Loads a pre-trained transformer-based emotion classification model and performs prediction.
    """
    def __init__(self, model_checkpoint="aubmindlab/bert-base-arabertv02",
                 saved_model_dir=r"c:\Year 2\Y2- Block C\Complete_pipeline\models\emotion_model\Transformer_77",
                 device="cpu"):
        self.device = device
        self.label_map = {
            0: "happiness",
            1: "sadness",
            2: "anger",
            3: "surprise",
            4: "fear",
            5: "disgust",
            6: "neutral"
        }
        self.tokenizer = AutoTokenizer.from_pretrained(saved_model_dir)
        self.model = AutoModelForSequenceClassification.from_pretrained(saved_model_dir, ignore_mismatched_sizes=True)
        self.model.to(self.device)
        self.model.eval()

    def predict(self, sentences):
        """
        Predicts emotions for a list of sentences.
        """
        predictions = []
        for sentence in sentences:
            encoding = self.tokenizer(sentence, return_tensors="pt", truncation=True,
                                        padding="max_length", max_length=128)
            encoding = {k: v.to(self.device) for k, v in encoding.items()}
            with torch.no_grad():
                outputs = self.model(**encoding)
            pred_id = torch.argmax(outputs.logits, dim=-1).item()
            predictions.append(self.label_map.get(pred_id, "neutral"))
        return predictions

# ==============================
# 4. Pipeline: Putting It All Together
# ==============================
def main(input_path, output_csv, device="cpu"):
    """
    Main pipeline function.
    Processes the input (audio or transcript CSV), translates (bypassed),
    classifies emotions, and saves the output CSV.
    """

    # Handle YouTube URL
    if input_path.startswith("http"):
        print("YouTube URL detected. Downloading audio...")
        input_path = download_audio_from_youtube(input_path)
        print(f"Audio downloaded to: {input_path}")
        # Handle audio file
    audio_extensions = (".mp3", ".wav", ".mp4")
    if input_path.lower().endswith(audio_extensions):
        print("Input detected as audio. Running speech-to-text...")
        stt_results = transcribe_audio(input_path, device=device)
        if not stt_results:
            print("No transcription generated.")
            return
        df = pd.DataFrame(stt_results)
    else:
        print("Input detected as transcript CSV.")
        df = pd.read_csv(input_path)
        if "Sentence" not in df.columns:
            raise ValueError("CSV file must contain a 'Sentence' column.")

    # Translation step: currently bypassed.
    print("Translating sentences (bypassed, filling with 'translation error')...")
    sentences = df["Sentence"].tolist()
    translated_sentences = translate_sentences(sentences, device=device)
    df["Translation"] = translated_sentences

    # Emotion Classification
    print("Classifying emotions...")
    classifier = EmotionClassifier(device=device)
    predicted_emotions = classifier.predict(translated_sentences)
    df["Emotion"] = predicted_emotions

    # Ensure that time columns exist
    if "Start Time" not in df.columns:
        df["Start Time"] = "00:00:00,000"
    if "End Time" not in df.columns:
        df["End Time"] = "00:00:00,000"

    final_columns = ["Start Time", "End Time", "Sentence", "Translation", "Emotion"]
    final_df = df[final_columns]
    final_df.to_csv(output_csv, index=False, encoding="utf-8-sig")
    print(f"Pipeline complete. Final output saved to: {output_csv}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="End-to-end pipeline for emotion classification.")
    parser.add_argument("--input", type=str, required=True,
                        help="Path to input audio file (e.g., .mp3, .wav, .mp4) or transcript CSV file.")
    parser.add_argument("--output", type=str, default="final_output.csv",
                        help="Path to save the final CSV output.")
    parser.add_argument("--device", type=str, default="cuda" if torch.cuda.is_available() else "cpu",
                        help="Device to run the pipeline on (e.g., 'cuda' or 'cpu').")
    args = parser.parse_args()
    main(args.input, args.output, device=args.device)