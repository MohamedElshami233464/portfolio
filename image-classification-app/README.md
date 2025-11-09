# 🍎 Image Classifier App — Deep Learning for Fruit Freshness Detection

---

## 🧭 Project Overview

The **Image Classifier App** is a deep learning application that classifies fruit images into **fresh vs. rotten apples and bananas**.  
It was developed following the **CRISP-DM framework**, integrating both **technical AI modeling** and **human-centered design principles** such as fairness, explainability, and usability testing.

This project demonstrates the full AI development cycle — from market research and data collection to model deployment and A/B user testing.

---

## 🎯 Objectives

- Design a machine learning system to **automatically assess fruit quality**.  
- Apply **CRISP-DM** stages: Business Understanding, Data Preparation, Modeling, Evaluation, and Deployment.  
- Build, test, and compare **deep learning architectures** for image classification.  
- Ensure **Responsible AI** through bias analysis and fairness evaluation.  
- Incorporate **Explainable AI (XAI)** methods for interpretability.  
- Deliver a **user-centered interface** with A/B testing feedback.

---

## 🧩 Methodology — CRISP-DM Framework

### 1. Business Understanding  
- Defined the business problem: automating fruit inspection to improve efficiency and reduce manual labor.  
- Identified key stakeholders: **fruit producers, retailers, and grocers**.  
- Created a **DAPS diagram** and **Power–Interest grid** to map stakeholder needs.  
- Determined value: reducing inspection time and improving customer satisfaction.

### 2. Data Understanding & Preparation  
- Collected dataset of ~800 images across 4 classes:
  - Fresh Apple 🍏  
  - Rotten Apple 🍎  
  - Fresh Banana 🍌  
  - Rotten Banana 🍌  
- Used web scraping via a Google Image scraper.  
- Performed manual cleaning and resizing to 224×224 px.  
- Addressed dataset bias:
  - Balanced classes through **data augmentation** (rotation, flipping, zoom).  
  - Adjusted color sensitivity (RGB normalization).  

### 3. Modeling & Implementation  
Implemented and compared multiple architectures:
| Iteration | Model | Description | Accuracy |
|------------|--------|--------------|-----------|
| 1 | MLP (Dense Network) | Simple baseline | 76.5% |
| 2 | CNN (Custom) | Added convolutional + pooling layers | 88.9% |
| 3 | CNN + Data Augmentation | Improved generalization | 92.5% |
| 4 | **VGG16 (Transfer Learning)** | Fine-tuned pre-trained model | **97.3%** ✅ |

### 4. Responsible AI  
- Detected dataset bias (age, color intensity, dataset composition).  
- Applied **Fairness-Through-Awareness** technique to ensure balanced learning.  
- Used **Explainable AI (XAI)** methods:
  - **LIME** — to visualize pixel regions influencing predictions.  
  - **Grad-CAM** — to generate heatmaps showing model focus areas.  
- Documented transparency trade-offs between interpretability and accuracy.

### 5. Evaluation  
- Evaluated models using:
  - Accuracy, Precision, Recall, F1-score  
  - Confusion Matrix visualization  
- Conducted **user testing**:
  - **Think-aloud sessions** to assess usability.  
  - **A/B testing** to compare two UI prototypes.  
  - Collected user feedback for design improvements.

### 6. Deployment  
- Delivered a functional **mobile app prototype** with real-time camera classification.  
- UI built for simplicity and clarity:
  - Users can take/upload photos  
  - Instant prediction display  
  - History log of classified images  

---

## 📊 Key Results

- Achieved **97.3% classification accuracy** using VGG16 with transfer learning.  
- Reduced overfitting via augmentation and dropout.  
- Generated interpretable Grad-CAM visualizations for model transparency.  
- Verified fairness and dataset balance post-augmentation.  
- Positive user feedback in A/B tests on clarity and speed.

---

## 🎨 Prototype & User Testing

Two interactive UI prototypes were designed and evaluated through **A/B user testing** using Figma.  
These interfaces allow users to capture or upload fruit images and instantly see model predictions (fresh vs. rotten).

| Version | Description | Link |
|----------|--------------|------|
| **Version A** | Initial app design focusing on basic functionality and layout. | [View on Figma](https://www.figma.com/proto/tDHK37CHeQ40t4z3PkEEjh/Version-A?node-id=0-1&t=kUVsp0lDGjABtqGr-1) |
| **Version B** | Improved layout with better contrast, icons, and interaction flow based on user feedback. | [View on Figma](https://www.figma.com/proto/9hvN1cpVybrcTXQEJjRaOx/version-B?t=kUVsp0lDGjABtqGr-1) |

**A/B Test Findings:**
- Version B scored higher in clarity, color balance, and ease of use.  
- 80% of test users preferred Version B for visual hierarchy and feedback clarity.  
- Both versions demonstrated consistent prediction accuracy and smooth flow.

---


## 🧠 Tools & Technologies

| Category | Tools / Libraries |
|-----------|-------------------|
| Deep Learning | TensorFlow / Keras, CNN, VGG16 |
| Explainability | LIME, Grad-CAM |
| Responsible AI | Fairness-Through-Awareness |
| Data Handling | Pandas, NumPy, OpenCV |
| Visualization | Matplotlib, Seaborn |
| Interface & UX | Figma / Prototype design |
| Evaluation | Accuracy, F1, Confusion Matrix |
| Framework | CRISP-DM |

---
## 🏆 Achievements

- ✅ Built and evaluated 4 neural network architectures.  
- ✅ Reached **97.3% accuracy** on test set.  
- ✅ Applied **Responsible AI** and **Explainable AI** principles.  
- ✅ Conducted **A/B user testing** for interface usability.  
- ✅ Demonstrated **efficiency enhancement** for retail automation.

---
## 💬 Reflection

This project strengthened my understanding of:
- End-to-end **AI system design** under the **CRISP-DM** structure.  
- How to implement fairness, transparency, and interpretability in ML pipelines.  
- The importance of combining **user experience testing** with **technical model evaluation**.  

It reflects not only technical growth in **deep learning** but also awareness of **ethical AI design**.

---

## 🔗 Contact

- 📧 **melshami909@gmail.com**  
- 🔗 [LinkedIn](https://www.linkedin.com/in/mohamed-elshami)  
- 💻 [Portfolio Website](https://mohamedelshami233464.github.io/)  
- 🧠 [GitHub Portfolio](https://github.com/MohamedElshami233464)

---
