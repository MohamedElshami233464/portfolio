# 🚗 ANWB Road Safety Risk Prediction — Breda

---

## 🧭 Overview

The **ANWB Road Safety Risk Prediction** project aims to **enhance driver safety in Breda** by predicting danger zones using AI and machine learning.  
By combining **ANWB driving behavior data**, **KNMI weather records**, and **Open Meteo rainfall data**, the project identifies high-risk areas and visualizes them for drivers in an accessible dashboard and app.

---

## 🎯 Objectives

- Improve road safety by detecting high-risk areas using AI.
- Integrate diverse datasets to find links between **driving behavior** and **weather conditions**.
- Design a functional **prototype interface** that informs drivers about dangerous roads.
- Ensure the system is **ethical, explainable, and compliant** with EU AI and GDPR laws.

---

## 🧠 Methodology (CRISP-DM)

### 1. **Business Understanding**
Road safety is a major concern in Breda.  
The team aimed to create a **predictive and explainable system** that highlights accident-prone zones, reducing the number of incidents.

### 2. **Data Understanding & Preprocessing**
Datasets used:
- **ANWB Dataset** – Driving behavior (speeding, harsh braking, cornering, acceleration).  
- **KNMI Dataset** – Weather data from Dutch meteorological sources.  
- **Open Meteo Dataset** – Rain and snow intensity data (2015–2024).

Preprocessing steps included:
- Handling missing values and outliers  
- Converting timestamps to datetime  
- Normalizing speed and duration values  
- Creating new features:
  - `avg_speed`
  - `incident_risk_level` (low/mid/high)
- Removing irrelevant columns (municipality name, lat/long)
- Log transformation for skewed columns

---

## ⚙️ Machine Learning Models

### Models Tested
| Model | Description | Accuracy / Performance |
|--------|--------------|------------------------|
| Decision Tree | Basic classification | ~91% |
| Random Forest | Ensemble model, feature importance | **98.8%** ✅ |
| Deep Neural Network (DNN) | Multilayer perceptron | 98.8% |
| K-Means | Unsupervised clustering | Risk segmentation |
| Gradient Boosting | Iterative improvement | 97% |

**Evaluation Metrics:** Accuracy, Precision, Recall, F1-score, ROC AUC

**Feature Importance:**  
- Average speed  
- Duration of incident  
- Weather risk level  
- Rain/snow intensity  

---

## 🧩 Responsible AI & Legal Considerations

- Complied with **EU AI Act** risk classification for transportation AI systems.  
- Conducted **GDPR compliance check** — no personal data used.  
- Applied **Responsible AI** principles:
  - Transparency  
  - Explainability (SHAP, XAI tools)  
  - Fairness  
  - Reproducibility  

---

## 💡 Interface Design (A/B Testing)

Two Figma interface prototypes were designed and tested:

| Version | Description | Result |
|----------|--------------|--------|
| Version A | Original design with basic layout | Avg. usability: 5.8/7 |
| Version B | Enhanced layout, RAAI (Road Assistance AI) button | **Preferred by users** ✅ |

- 30 users participated in testing (Likert scale 1–7)
- **Version B** scored higher across all dimensions (usability, clarity, enjoyment)
- Introduced a **RAAI feature** for AI-based assistance and notifications

Figma links:
- [Version A](https://www.figma.com/proto/jzar4rAjbEHxkHtHvmMR77/Version-A---RAAI--Road-Assistance-with-Artificial-Intelligence-?node-id=0-1&t=noJ1TYxXVhNsFrSX-1)
- [Version B](https://www.figma.com/proto/e6XppffUkrFvZaY0NPiN9Q/Version-B---RAAI--Road-Assistance-with-Artificial-Intelligence-?node-id=0-1&t=SrZLSi0QvxMfQ7Di-1)

---

## 🧪 Deployment & Testing

- Built **Poetry virtual environment** for isolated dependency management.  
- Created `pyproject.toml` and `Poetry.lock` files.  
- Added unit tests (`test_main_script.py`) achieving **55% code coverage**.  
- Deployed app prototype to a cloud environment.  
- Used logging (`pylint`, `flake8`) and documentation (`Sphinx`) for maintainability.

---

## 📊 Results & Key Insights

- **Main hotspot:** Graaf Engelbertlaan (over 4500 incidents)
- **Most common cause:** Speeding (75% of all incidents)
- **Peak risk period:** May 2018
- **Weather link:** Rain intensity > 10mm strongly correlated with high-risk levels

---

## 🧰 Tools & Technologies

| Category | Tools |
|-----------|--------|
| Languages | Python, SQL |
| ML Libraries | scikit-learn, TensorFlow, XGBoost |
| Data Tools | pandas, NumPy, matplotlib, seaborn |
| Deployment | Poetry, UnitTest, Coverage.py |
| Design | Figma, PowerPoint |
| Version Control | GitHub, SharePoint, Trello |

---

## 🏆 Achievements

- Built an AI-powered risk prediction pipeline for safer roads in Breda.  
- Integrated 3 major datasets (ANWB, KNMI, Open Meteo).  
- Achieved **98.8% accuracy** using Random Forest & DNN.  
- Designed, tested, and deployed two user interfaces.  
- Implemented 55% code coverage via unit testing.  
- Ensured compliance with **EU AI Act** and **GDPR**.

---

## 🔗 Contact

- 📧 **melshami909@gmail.com**  
- 🔗 [LinkedIn](https://www.linkedin.com/in/mohamed-elshami)  
- 💻 [Portfolio Website](https://mohamedelshami233464.github.io/)

---
