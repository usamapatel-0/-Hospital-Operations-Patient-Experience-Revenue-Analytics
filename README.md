# Hospital Operations, Patient Experience & Revenue Analytics

## 📌 Project Overview

This project is an end-to-end healthcare data analytics project focused on hospital operations, patient experience, revenue, treatment patterns, and readmissions.

The project demonstrates how raw healthcare data can be transformed into meaningful business insights using:

- Excel
- Python
- SQL
- Statistics
- Power BI
- Tableau

> **Note:** This project uses synthetic healthcare data created for portfolio and learning purposes. It does not contain real patient information.

---

## 🎯 Business Questions

- Which departments receive the most admissions?
- Which departments generate the highest revenue?
- Which treatments have the highest average billing?
- How does length of stay relate to hospital billing?
- What is the 30-day readmission rate?
- How does readmission vary across departments?
- Which insurance types contribute the most revenue?
- Which diagnoses are most common in the hospital?
- How do admissions change over time?
- What is the average patient rating?

---

## 🏗️ Project Architecture

<img width="1655" height="950" alt="Architecture_Hospital" src="https://github.com/user-attachments/assets/8e23594d-04f0-4b6f-b0a2-71a0bfa0a55e" />

### Workflow

Raw Healthcare Data  
↓  
Python Data Cleaning & Exploratory Analysis  
↓  
Cleaned Healthcare Dataset  
↓  
Excel + SQL + Statistics + Python Analysis  
↓  
Power BI Dashboard  
↓  
Tableau Dashboard  
↓  
Business Insights

---

## 📌 Dataset

The project contains **15,000 synthetic hospital admission records** with **23 columns**.

Key fields include:

- Patient ID
- Admission ID
- Age
- Gender
- Department
- Admission Date
- Discharge Date
- Diagnosis
- Treatment
- Admission Type
- Insurance Type
- Total Bill
- Length of Stay
- Patient Rating
- Outcome
- 30-Day Readmission

---

## 🐍 Python Analysis

Python was used for:

- Data loading
- Data cleaning
- Data quality checks
- Exploratory Data Analysis
- Descriptive statistics
- Outlier analysis
- Correlation analysis
- Hypothesis testing
- Data visualization

### Libraries Used

- Pandas
- NumPy
- SciPy

---

## 🗄️ SQL Analysis

SQL was used to answer business questions and calculate important hospital KPIs.

### Analysis Included

- Total admissions
- Admissions by department
- Average bill by department
- Total revenue by department
- Average length of stay
- Revenue by insurance type
- Average bill by treatment
- Monthly admissions
- 30-day readmission percentage
- High-billing cases

### SQL Concepts Used

- SELECT
- WHERE
- GROUP BY
- ORDER BY
- COUNT
- SUM
- AVG
- ROUND
- Subqueries
- Date functions

---

## 📗 Excel Analysis

Excel was used for management-level analysis and KPI preparation.

### Excel Work Included

- Data profiling
- Data cleaning
- KPI calculations
- PivotTables
- PivotCharts
- SUMIFS
- COUNTIFS
- AVERAGEIFS
- Dashboard preparation
  <img width="1917" height="993" alt="Excel_Dashboard" src="https://github.com/user-attachments/assets/d67b4c34-b2eb-472d-bac6-58389ad15eb9" />


---

## 📐 Statistical Analysis

Statistical techniques used in the project include:

- Descriptive statistics
- Correlation analysis
- Independent samples t-test
- ANOVA
- Chi-square test
- 95% confidence interval
- Outlier analysis

### Statistical Results

**T-Test**

- T-statistic: 0.035
- P-value: 0.972

The tested group means did not show a statistically significant difference at the 5% significance level.

**ANOVA**

- F-statistic: 550.556
- P-value: < 0.001

The results indicate a statistically significant difference among at least some of the tested group means.

**Chi-Square Test**

- Chi-square statistic: 13.909
- P-value: 0.001

The tested categorical variables showed a statistically significant association.

---

# 📊 Power BI Dashboard

<img width="1146" height="637" alt="Dashboard" src="https://github.com/user-attachments/assets/827b43f3-97b8-43a5-8af1-79536f071b18" />

The Power BI dashboard provides an interactive overview of hospital operations, revenue, patient experience, and readmission patterns.

### Dashboard Visualizations

- Admissions by Department
- Revenue by Department
- Monthly Admissions
- Average Bill by Treatment
- Readmission by Department
- Revenue by Insurance
- Average Bill by Length of Stay

### Key KPIs

| KPI | Value |
|---|---:|
| Total Admissions | 15,000 |
| Total Revenue | ₹965.49M |
| Average Bill | ₹64.37K |
| Average Length of Stay | 4.87 Days |
| 30-Day Readmission Rate | 11.86% |

---

# 📈 Tableau Dashboard

<img width="1010" height="803" alt="Tableau Dashboard" src="https://github.com/user-attachments/assets/21dbafd0-d99f-410d-a178-4c94c3c580ae" />

A Tableau dashboard was also created using the cleaned healthcare dataset to provide an additional interactive visualization layer.

### Tableau Visualizations

- Admissions by Department
- Readmission by Department
- Revenue by Insurance Type
- Average Bill by Length of Stay
- Total Admissions KPI

Tableau was used to demonstrate dashboard development and visualization skills across multiple Business Intelligence tools.

---

## 🔍 Key Findings

- General Medicine recorded the highest number of admissions.
- Oncology had the highest average bill among departments.
- General Medicine generated the highest total department revenue.
- Surgery had the highest average bill among treatments.
- Private insurance contributed the largest share of total billing.
- Overall 30-day readmission rate was 11.86%.
- Patient ratings averaged approximately 3.98 out of 5.
- Hospital billing generally increased with longer length of stay, although individual length-of-stay groups showed variation.
- The most common diagnoses included Heart Disease, Skin Infection, Migraine, Pneumonia, and Hypertension.

> These findings are descriptive and do not establish causation.

---

## 📂 Project Structure

```text
Healthcare DataAnalyst Project/
│
├── data/
│   ├── raw/
│   └── cleaned/
│       └── healthcare_cleaned.csv
│
├── excel/
│   └── healthcare_cleaned.xlsx
│
├── powerbi/
│   └── dashboard_healthcare.pbix
│
├── tableau/
│   └── healthcare_dashboard.twbx
│
├── python/
│   └── healthcare_EDA.ipynb
│
├── sql/
│   ├── healthcare.db
│   ├── queries.sql
│   └── sql_analysis.py
│
├── screenshots/
│   ├── architecture.png
│   ├── powerbi_dashboard.png
│   └── tableau_dashboard.png
│
├── .gitignore
└── README.md
```
## 🛠️ Tools & Technologies

| Tool | Purpose |
|---|---|
| Excel | Data cleaning, PivotTables, PivotCharts and KPI analysis |
| Python | Data cleaning, EDA and statistical analysis |
| Pandas | Data manipulation |
| NumPy | Numerical analysis |
| SciPy | Statistical analysis |
| SQL | Business analysis and KPI queries |
| Power BI | Interactive dashboard |
| Tableau | Interactive dashboard and visualization |
| GitHub | Project documentation and portfolio |

---

## ⚠️ Data Disclaimer

This project uses synthetic healthcare data for educational and portfolio purposes.

The dataset does not represent real hospital patients or real-world hospital performance.

High billing values were reviewed as potential outliers but were not automatically removed because high healthcare costs can represent legitimate cases.

---

## 🚀 Skills Demonstrated

- Healthcare Analytics
- Data Cleaning
- Exploratory Data Analysis
- Statistical Analysis
- SQL
- Excel
- Power BI
- Tableau
- Data Visualization
- Business Intelligence
- KPI Development
- Data Storytelling
- Business Problem Solving

---

## 👤 Project Type

**Portfolio Project | Healthcare Data Analytics | Synthetic Dataset**
