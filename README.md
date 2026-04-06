# bda-modulo-3-evaluacion-final-iramana8
bda-modulo-3-evaluacion-final-iramana8 created by GitHub Classroom

# Airline Loyalty Program Analysis

This project is the final assessment of **Module 3: Transforming Data** in the Adalab Data Analytics & AI bootcamp.

---

## Overview

The objective of this project is to analyze an airline loyalty program dataset by applying data transformation, cleaning, statistical analysis, and visualization techniques.

The analysis follows a structured workflow divided into three main phases:

1. Data Exploration & Transformation  
2. Statistical Analysis  
3. Data Visualization  

The goal is not only to prepare and transform the data, but also to extract meaningful insights about customer behavior and communicate them clearly in a business-oriented way.

---

## Dataset Context

The analysis is based on two datasets related to an airline loyalty program:

### Customer Flight Activity

This dataset contains monthly information about customer activity, including:
- Flights booked  
- Distance traveled  
- Loyalty points accumulated and redeemed  

Each row represents a **customer-month record**, meaning the same customer appears multiple times across different time periods.

### Customer Loyalty Profile

This dataset contains customer-level information such as:
- Location (province, city)  
- Education level  
- Salary  
- Marital status  
- Loyalty card type  

Each row represents a **unique customer**.

---

## Project Structure

```bash
files/
├── raw/                  # Original datasets
├── processed/            # Cleaned datasets

notebooks/
├── 01_eda_and_transformation.ipynb
├── 02_statistical_analysis.ipynb
└── 03_visualizations.ipynb

src/
├── support_stadistics.py
└── support_visualizations.py

README.md