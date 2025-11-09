# Complete Pipeline for Emotion Classification

This repository contains an end-to-end NLP pipeline that:

1. Transcribes audio files using OpenAI Whisper (if audio input is provided).
2. Translates Arabic text to English using a custom fine-tuned translation model (if desired).
3. Classifies emotions in text using a transformer-based classifier.
4. Outputs a CSV file with the columns:  
   **Start Time, End Time, Sentence, Translation, and Emotion.**

---

## Table of Contents

- [Project Structure](#project-structure)
- [Environment Setup](#environment-setup)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

---

## Project Structure

| File/Directory          | Description                                                                 |
|-------------------------|-----------------------------------------------------------------------------|
| **`pipeline.py`**       | Main script to execute the entire pipeline.                                 |
| **`models/`**           | Contains all trained/fine-tuned models:                                     |
| → `classification_model/`      | - Emotion classification model (e.g., `Transformer_77`).                   |
| → `translation_model/`  | - Translation model (e.g., `final_model`).                                 |
| **`data/`**             | Stores input data files (e.g., `merged_whisper.csv`).               |
| **`requirements.txt`**  | Lists Python dependencies to install.                                      |
| **`README.md`**         | Project documentation (this file).                                         |
| **`final_output.csv`**  | Output file generated after running the pipeline.                          |

- **pipeline.py**: Main script to run the pipeline.
- **models/**: Contains the saved/fine-tuned models for translation and emotion classification.
- **data/**: Contains sample data files (e.g., CSV files for transcripts).
- **requirements.txt**: Lists the Python libraries needed for this project.
- **README.md**: Documentation (this file).

---

## Environment Setup

1. **Install Python**  
   Make sure you have [Python 3.8+](https://www.python.org/downloads/) installed.

2. **Create a Virtual Environment (Optional but Recommended)**

   **Using conda:**
    ```bash
    conda create -n y2c python=3.9
    conda activate y2c
    

**Or using venv:**

    
    python -m venv y2c
    source y2c/bin/activate   # Linux/Mac
    y2c\Scripts\activate      # Windows
    

2. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```
This will install all the required libraries, including:

- torch

- transformers

- whisper

- sentencepiece

- pandas

- numpy

- tqdm (optional for progress bars)

- sacremoses (recommended for certain translation models)

---

## Installation
1. Clone or Download this repository to your local machine.

2. Navigate to the root directory (where pipeline.py is located).

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```
4. Ensure you have FFmpeg installed and available in your system PATH.

---

# Usage
The pipeline supports two types of inputs:

1. Audio File (e.g., *.mp3, *.wav, *.mp4)

- The pipeline will transcribe the audio using Whisper, then proceed with translation and emotion classification.

2. Transcript CSV File

- The CSV file should contain at least a Sentence column. If Start Time and End Time columns are also present, the pipeline will use them. Otherwise, it will default to 00:00:00,000.

3. YouTube URLs

-  Downloads and extracts audio automatically, then processes it like a regular audio file.

# Running the Pipeline
Use the following command:

    
    python pipeline.py --input "<PATH_OR_URL>" --output "<OUTPUT_CSV>" --device cuda
    
 - input: Path to the input file (URL, audio file, or CSV).

 - output: Path to the output CSV (default is final_output.csv).

 - device: The device to run on. Use "cpu" if you do not have a GPU or "cuda" if you have a compatible GPU.

### Examples
    
- Using a YouTube URL:
```bash
python pipeline.py --input "https://youtu.be/Q9Hmo3EsvXA?si=ftjgH-Ci7B74jFeC" --output "final_output.csv" --device cpu
```
- Using a local audio file:
```bash
python pipeline.py --input "data/episode1.mp3" --output "final_output.csv" --device cuda
```
- Using a transcript CSV:
```bash
python pipeline.py --input "data/merged_whisper.csv" --output "final_output.csv" --device cpu
```
---

# License
This project is provided for educational purposes and does not include a specific open-source license. For questions about usage or licensing, please contact the author or maintainers of this repository.