# Week 3: Python & Data Wrangling

## 📌 Project Overview
This repository contains the **Week 3 Assignment** focused on data cleaning and feature engineering using Pandas, Matplotlib, and Seaborn on a messy health/workout dataset.

---

## 🛠️ Data Cleaning Steps Applied
1. **Date Standardisation**: Cleaned single-quoted date strings and converted values to standard `datetime64[ns]` format.
2. **Missing Value Imputation**: Filled missing `Calories` entries using median imputation ($291.2$ kcal) and removed rows missing critical date entries.
3. **Outlier Correction**: Identified and corrected an extreme workout duration outlier ($450$ minutes $\rightarrow$ $45$ minutes).
4. **Deduplication**: Removed exact row duplicates.
5. **Feature Engineering**: Created `Calorie_Burn_Rate` ($\text{Calories} / \text{Duration}$) to analyze workout intensity.

---

## 📁 Repository Structure
```text
├── data.csv                 # Raw input dataset
├── cleaned_health_data.csv  # Cleaned output dataset
├── workout_analysis.png     # Scatter plot visualization
└── README.md                # Project documentation
