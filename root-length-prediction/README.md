# 🌱 Root Length Prediction – Computer Vision & Robotics Project

**Author:** Mohamed Elshami  
**Program:** BSc Applied Data Science & Artificial Intelligence (BUas)  
**Client:** Netherlands Plant Eco-phenotyping Centre (NPEC)  
**Focus:** Deep Learning • Computer Vision • Automation  

---

## 🧭 Project Overview

This project was developed in collaboration with the **Netherlands Plant Eco-phenotyping Centre (NPEC)** to automate the measurement of **plant root lengths** using **computer vision** and **deep learning**.

The goal was to process thousands of microscope images of *Arabidopsis thaliana* seedlings grown in Petri dishes, segment the roots from the background, and automatically measure the **primary root length**.  
The final system supports large-scale agricultural research by reducing manual inspection time and improving accuracy.

---

## 🎯 Objectives

- Automate **root segmentation** and **root length measurement**.  
- Train a **U-Net deep learning model** to identify plant roots from high-resolution images.  
- Develop an **end-to-end image processing pipeline** for data cleaning, training, and prediction.  
- Prepare results for integration with a **robotic inoculation system**.  
- Evaluate performance using metrics like **F1-score** and **sMAPE**.

---

## 🌿 Project Context

NPEC operates advanced phenotyping systems to study plant growth under controlled environments.  
The data used in this project comes from NPEC’s **Hades system**, which captures daily images of plant roots.  

Each Petri dish contains 5 seeds of *Arabidopsis thaliana*, photographed over several days as they grow and develop complex root systems.  
These images are large, high-resolution, and require both **preprocessing** and **AI-based segmentation** to extract meaningful measurements.

---

## ⚙️ Methodology

### 🧩 1. Data Preprocessing
Before training the model, several computer vision techniques were used to clean and prepare the dataset:
- Converted images to grayscale.  
- Applied **Gaussian blur** and **CLAHE** for better contrast.  
- Detected and cropped Petri dishes using **Otsu’s thresholding** and **contour detection**.  
- Removed noise and irrelevant regions near image borders.  
- Created binary masks for the regions containing plant roots.

These steps were implemented in the early notebooks (`task2.ipynb`, `task3.ipynb`).

---

### 🧠 2. Model Training (U-Net)
A **U-Net convolutional neural network** was trained to perform root segmentation at the pixel level.

**Key Details:**
- Frameworks: TensorFlow & Keras  
- Loss function: Dice + Binary Cross-Entropy  
- Optimizer: Adam  
- Data Augmentation: rotation, flipping, and zooming  
- Training data: Y2B_23 and Y2B_24 datasets  

**Results:**
- Validation **F1-score:** 0.7936  
- The model successfully generalized across test images, producing clean and accurate masks of root structures.  

Model weights were saved as:  
`unet_model_256px.h5`

---

### 🔍 3. Model Inference & Segmentation
The trained U-Net model was loaded to predict segmentation masks on unseen test data.  
Post-processing was used to refine these predictions:
- Applied morphological cleanup and contour detection.  
- Identified and separated overlapping root systems.  
- Saved binary masks visualizing detected roots.

Example output:  
The predicted root regions were accurately identified and separated from the Petri dish background, even in complex overlapping cases.

---

### 🌱 4. Root Length Measurement
After segmentation, a custom algorithm measured the **primary root length** for each plant:
1. Loaded predicted masks.  
2. Extracted individual root contours.  
3. Calculated root length in pixels, later converted to millimeters.  
4. Saved results to CSV for analysis.

This step produced reliable measurements used for benchmarking and comparison.

---

### 🧪 5. Kaggle Competition Results
To validate the model’s accuracy and generalization, predictions were submitted to a **Kaggle competition** hosted for this project.

**Performance:**
| Metric | Score |
|--------|--------|
| F1 (Validation) | 0.7936 |
| sMAPE (Private Leaderboard) | **27.0%** |
| Ranking | **59th out of 250+ participants** |

These results demonstrated a well-performing model capable of consistent and reproducible root segmentation and measurement.

---

### 🤖 6. Robotics Integration
The segmentation and measurement system was designed to integrate with the **Opentrons OT-2 robot**, which automates pipette-based inoculation.  
By providing precise root tip locations, the model enables targeted robotic actions, reducing manual intervention and improving experimental consistency.

---

## 🧰 Tools & Technologies

| Category | Tools / Libraries |
|-----------|------------------|
| Deep Learning | TensorFlow, Keras, PyTorch |
| Computer Vision | OpenCV, Scikit-image, NumPy |
| Data Processing | Pandas, Matplotlib |
| Metrics | F1-score, sMAPE |
| Robotics (Future Integration) | OpenAI Gym, PID control |
| Version Control | GitHub, W&B (Weights & Biases) |

---
## 💬 Reflection

This project was a deep dive into combining AI, computer vision, and robotics for a real-world biological problem.
It taught me how to handle large image datasets, train and fine-tune deep learning models, and translate predictions into meaningful real-world actions.

The experience strengthened my ability to:

- Design AI pipelines end-to-end

- Improve models through iterative testing

- Communicate results effectively

- Collaborate on interdisciplinary challenges involving AI and biology

---
## 🔗 Contact

- 📧 **melshami909@gmail.com**  
- 🔗 [LinkedIn](https://www.linkedin.com/in/mohamed-elshami)  
- 💻 [Portfolio Website](https://mohamedelshami233464.github.io/)

---
