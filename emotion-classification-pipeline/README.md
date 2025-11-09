# 🎭 Emotion Classification Pipeline (Arabic & English)

**Author:** Mohamed Elshami  
**Program:** BSc Applied Data Science & Artificial Intelligence (BUas)  
**Client:** Content Intelligence Agency  
**Focus:** Natural Language Processing (NLP) • Emotion Detection • Machine Translation  

---

## 🧭 Project Overview

This project focuses on building an **end-to-end NLP pipeline** that detects emotions in **Arabic and English video transcripts**.  
The system automatically processes video or audio content (e.g., TV shows, interviews, podcasts) and identifies the **emotional tone** of each spoken sentence.

The pipeline combines **speech-to-text**, **machine translation**, and **emotion classification** using modern AI models, enabling scalable and multilingual emotion detection for real-world media applications.

---

## 🎯 Objectives

- Build a full NLP pipeline capable of:
  1. Transcribing Arabic or English audio/video to text.  
  2. Translating Arabic sentences into English.  
  3. Classifying emotions (happiness, sadness, anger, fear, surprise, disgust).  
  4. Outputting tagged transcripts with timestamps and emotions.  
- Experiment with multiple machine learning and deep learning models.  
- Improve accuracy and interpretability through explainable AI (XAI).  
- Support the **Content Intelligence Agency** in analyzing emotional patterns in media.

---

## 🧩 Pipeline Overview

### 1. 🎙️ Speech Recognition
- Used **OpenAI Whisper** and **AssemblyAI** to transcribe Arabic and English audio into text.  
- The output transcript includes start and end timestamps for each sentence.

### 2. 🌐 Machine Translation
- Built a **custom fine-tuned transformer model** for **Arabic → English** translation.  
- Trained and validated using parallel Arabic–English datasets.  
- Notebook: `machine_translation.ipynb`

### 3. 💬 Emotion Classification
- Explored several models:
  - **Logistic Regression & Naïve Bayes** (baseline)
  - **LSTM** (sequence-based deep learning)
  - **Transformer models** (e.g., XLM-RoBERTa, AraBERT)
- The best-performing model achieved an **F1-score of 0.77** using **AraBERT** after tuning hyperparameters (batch size, epochs, label mapping).
- Notebook: `modelcard1.ipynb`

### 4. 🧠 Prompt Engineering & Explainability
- Applied **prompt engineering** to test zero-shot emotion detection using large language models (LLMs).
- Used **Explainable AI (XAI)** techniques like **LIME** and **Grad-CAM** to visualize token-level attention and improve interpretability.
- Notebook: `prompt_engineering.ipynb`

### 5. 📊 Results Aggregation & Summary
- Combined transcription, translation, and emotion classification results into a single CSV file.  
- Example output file: `final_output.csv`  
- Summarized project insights and evaluation metrics.
- Notebook: `task9_summarize.ipynb`

---

## 📈 Model Performance

| Model | Type | F1-score | Key Notes |
|--------|------|-----------|------------|
| Logistic Regression | Linear | 0.73 | Fast baseline |
| Naïve Bayes | Probabilistic | 0.74 | Good with sparse data |
| LSTM | Deep Learning | 0.72 | Captures sequential dependencies |
| RNN | Deep Learning | 0.32 | Struggled with context |
| Transformer (AraBERT) | Attention-based | **0.77** | Best overall accuracy and stability |

---

## 💡 Key Results

- ✅ Achieved **F1 = 0.77** with fine-tuned **AraBERT** model.  
- ✅ Built and tested an **Arabic–English translation module**.  
- ✅ Integrated **speech-to-text**, **translation**, and **emotion tagging** into one pipeline.  
- ✅ Implemented **explainable AI** methods to visualize model reasoning.  
- ✅ Provided a **client-ready solution** for emotion detection in media content.

---

## 🧰 Tools & Technologies

| Category | Tools / Libraries |
|-----------|------------------|
| NLP Models | Hugging Face Transformers, AraBERT, XLM-RoBERTa |
| Speech-to-Text | OpenAI Whisper, AssemblyAI |
| Translation | Custom Transformer, SentencePiece |
| Machine Learning | Scikit-learn, PyTorch |
| Data Handling | Pandas, NumPy |
| Explainability | LIME, Grad-CAM |
| Deployment | Python, FastAPI, CSV Output |
| Visualization | Matplotlib, Seaborn |

---
## 🧪 Example Output

| Start Time | End Time | Sentence (AR) | Translation (EN) | Emotion   |
|-----------:|---------:|:--------------|:-----------------|:----------|
| 00:00:01   | 00:00:05 | أنا سعيد اليوم | I am happy today | Happiness |
| 00:00:06   | 00:00:10 | هذا الخبر محزن جداً | This news is very sad | Sadness   |

## 🗣️ Use Case for the Client

This pipeline helps the Content Intelligence Agency:

- Analyze emotional trends in TV shows, films, and interviews.

- Automatically tag scenes by emotional tone for improved search and recommendations.

- Reduce manual labeling time and ensure consistency across datasets.

- Integrate the results into their existing LLM-powered media analysis systems.

## ⚙️ Running the Pipeline

You can run the pipeline end-to-end using:

    python pipeline.py --input "<PATH_TO_FILE>" --output "final_output.csv" --device cuda


It accepts:

- 🎧 Audio or video files (e.g., .mp3, .mp4)

- 📄 Transcript CSV files

- 🔗 YouTube URLs (downloads and processes automatically)

## 🚀 Achievements

- End-to-end working emotion detection system for Arabic and English content.

- Reached 0.77 F1-score with transformer-based models.

- Integrated explainability (LIME, Grad-CAM).

- Delivered a client-ready prototype for emotion-aware media analysis.

- Presented findings in a professional presentation and technical report.

## 💬 Reflection

This project helped me gain deep experience in:

- Natural Language Processing and multilingual modeling.

- Fine-tuning transformer models for low-resource languages like Arabic.

- Combining multiple AI components into one working pipeline.

- Understanding challenges around bias, fairness, and translation quality.

It showed me how real-world NLP solutions can connect technical accuracy with media insights and human emotion understanding.
