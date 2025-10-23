# ⚽ NAC Breda — Player Analytics & Market Value Modeling

**Author:** [Mohamed Elshami](https://github.com/MohamedElshami233464)  
**Course:** Applied Data Science & Artificial Intelligence — Year 1 Block B (BUas)  
**Date:** January 2024 

---

## 🧭 Project Overview

This project focuses on analyzing **NAC Breda player performance and market value** using real football data.  
It combines **data cleaning, exploratory data analysis (EDA), feature selection, and machine learning modeling** to understand which factors influence a player's market value.

The project was developed as part of **Block B: Data Science & Machine Learning**, following the **CRISP-DM** process.

---

## 🎯 Objectives

- Explore patterns between **player attributes** (age, goals, assists, expected goals/xG, contracts, etc.) and **market value**  
- Identify **key performance indicators (KPIs)** that influence player valuation  
- Build and evaluate several **machine learning models** to predict player market value  
- Deliver a clear and professional **report and visual dashboard** for interpretation

---

## 🧠 Methodology

The analysis followed a **CRISP-DM** inspired workflow:

1. **Business Understanding**  
   Understand NAC Breda’s needs to identify key factors behind player valuation.

2. **Data Preparation**  
   - Cleaned and combined 16K+ player records (missing values, duplicates, type conversions).  
   - Exported a unified dataset: `Combined_DATA.csv`.

3. **Exploratory Data Analysis (EDA)**  
   - Visualized correlations and trends:
     - Market value vs. age  
     - Height, weight vs. goals  
     - Expected goals (xG) vs. actual goals  
     - Contract duration left per player  
     - Matches played by age group  
     - Player age distribution and top countries  

4. **Feature Selection**  
   Using **SelectKBest**, identified top features for predicting market value:  
   `Goals`, `xG`, `Assists`, `xA`, `Non-penalty goals`

5. **Modeling**  
   - Tested and compared multiple ML models:
     - Linear Regression ✅ (Best performing, interpretable)
     - Random Forest
     - Gradient Boosting
     - XGBoost
     - SVM (exploratory baseline)
   - Applied **PCA** to reduce dimensionality — improved MSE slightly.

6. **Evaluation**  
   - **Metric:** Mean Squared Error (MSE)  
   - Best result: **PCA + Linear Regression → MSE ≈ 1.62×10¹²**

7. **Reporting & Visualization**  
   - Created full report (PDF)  
   - Exported professional Power BI visuals  
   - Included in GitHub for transparency and reproducibility  

---

## 📊 Key Insights

- Player **market value peaks in mid-20s** but varies widely by performance.  
- **xG vs. Goals** shows finishing consistency or underperformance.  
- **Physical attributes** (height/weight) show moderate positive trends with goals.  
- **Contract duration** visualization identifies short-term renewal risks.  
- Linear models outperform tree-based ones due to smaller feature set and interpretability.

---

## 🤖 Machine Learning Results

| Model | Metric | Result |
|-------|---------|--------|
| Linear Regression | MSE | **1.67e12** |
| PCA + Linear Regression | MSE | **1.62e12** |
| Random Forest | MSE | 1.91e12 |
| Gradient Boosting | MSE | 1.78e12 |
| XGBoost | MSE | 1.75e12 |

✅ **Best model:** Linear Regression with PCA  
Simple, interpretable, and achieves lowest MSE.

---

## 🧩 Tools & Libraries

- **Python (Jupyter Notebook)**  
  `pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`, `xgboost`, `sympy`
- **Power BI** — for visualization dashboards  
- **GitHub** — for version control and portfolio presentation  

---

## 📚 Learning Achievements

While developing this project, I completed several **DataCamp certifications** to strengthen my foundation in data analysis and machine learning:

### 🏅 Certificates:
- **Data Manipulation with pandas**
- **Data Visualization with Matplotlib**
- **Machine Learning with Tree-Based Models**
- **Understanding Machine Learning**
- **Cluster Analysis in Python**
- **Dimensionality Reduction in Python**
- **Introduction to Importing Data**
- **Unit Testing for Data Science in Python**

