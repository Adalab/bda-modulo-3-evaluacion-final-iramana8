# bda-modulo-3-evaluacion-final-iramana8
bda-modulo-3-evaluacion-final-iramana8 created by GitHub Classroom

# Airline Loyalty Program Analysis

## Overview

This project is the final assessment of Module 3: Transforming Data from a Data Analytics bootcamp.

The objective of this project is to analyze an airline loyalty program dataset by applying data transformation, cleaning, statistical analysis, and visualization techniques.

The project follows a structured analytical workflow divided into three main phases:

1. Data Exploration & Transformation
2. Statistical Analysis
3. Data Visualization

The goal is not only to manipulate and prepare the data, but also to extract meaningful insights about customer behavior and communicate them clearly in a business-oriented way.

---

## Dataset Context

The analysis is based on two datasets related to an airline loyalty program:

### Customer Flight Activity

This dataset contains monthly information about customer flight activity, including:
- Number of flights booked
- Distance traveled
- Loyalty points accumulated and redeemed

Each row represents a customer-month record, meaning the same customer appears multiple times across different months and years.

### Customer Loyalty Profile

This dataset includes customer-level information such as:
- Location (province, city)
- Education level
- Salary
- Marital status
- Loyalty card type

Each row represents a unique customer.

---

## Project Structure

files/
├── raw/            # Original datasets
├── processed/      # Cleaned datasets

notebooks/
├── 01_eda_and_transformation.ipynb
├── 02_statistical_analysis.ipynb
├── 03_visualizations.ipynb

src/
├── support_stadistics.py
├── support_visualizations.py

README.md

---

## Phase 1 — Data Exploration & Transformation

In this phase, both datasets were explored to understand their structure and identify data quality issues. The main focus was on preparing and transforming the data to make it suitable for analysis.

Main tasks performed:

- Initial data exploration:
  - dataset structure
  - data types
  - null values
  - duplicates

- Dataset merge using the customer identifier

- Handling missing values:
  - Salary cleaned and imputed using median by education group and global fallback
  - Cancellation variables kept as null because they represent non-cancelled customers

- Duplicate handling:
  - exact duplicates removed
  - inconsistent duplicates analyzed and documented instead of being modified

- Data consistency checks:
  - validation of relationships between variables such as Total Flights

- Final preparation of the dataset for analysis

This phase ensures that the dataset is reliable, consistent, and ready for further analytical work.

---

## Phase 2 — Statistical Analysis

In this phase, the dataset is analyzed using descriptive statistics and correlation analysis.

Numerical analysis includes:
- mean
- median
- mode
- standard deviation
- minimum and maximum values
- outlier detection using IQR
- correlation matrix visualization

Key insights:
- strong relationship between distance and accumulated points
- high variability in flight activity, with a small group of highly active customers

Categorical analysis includes:
- frequency distribution of variables such as:
  - Province
  - Education
  - Loyalty Card
  - Marital Status

Key insights:
- customer base is concentrated in specific regions and categories

---

## Phase 3 — Data Visualization

In this phase, visualizations are created to answer key business questions and communicate insights clearly.

All visualizations are generated using a custom class located in:

src/support_visualizations.py

This allows:
- consistent styling using viridis palette
- clean and reusable code
- separation between analysis and visualization logic

Key visualizations:

- Flights booked by month → identifies seasonality patterns
- Distance vs points → shows strong positive relationship
- Customers by province → highlights geographical concentration
- Salary by education → reveals socioeconomic differences
- Loyalty card distribution → shows concentration in specific tiers
- Marital status and gender → describes customer demographics

---

## Key Insights

- flight activity is not evenly distributed throughout the year
- loyalty points are strongly driven by distance traveled
- customers are geographically concentrated in specific provinces
- higher education levels are associated with higher average salaries
- most customers are concentrated in a limited number of loyalty tiers
- demographic distribution is relatively balanced across gender

---

## Technologies Used

- Python
- Pandas
- NumPy
- Seaborn
- Matplotlib
- Jupyter Notebook

---

## How to Run the Project

1. Clone this repository
2. Install dependencies:

pip install pandas numpy matplotlib seaborn

3. Open the notebooks in order:
   - 01_eda_and_transformation.ipynb
   - 02_statistical_analysis.ipynb
   - 03_visualizations.ipynb

---

## What This Project Demonstrates

- data transformation and preprocessing skills
- ability to detect and handle data inconsistencies
- statistical reasoning and interpretation
- data visualization for business insights
- code organization using reusable modules
- clear communication of analytical results

---

## Final Note

This project represents a complete data analysis workflow, from raw data transformation to insight generation and visualization. It reflects how real-world data projects are structured and how analytical results can be communicated effectively to both technical and non-technical audiences.