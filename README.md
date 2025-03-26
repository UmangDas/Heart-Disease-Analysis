# Heart Disease Analysis

## Getting Started
This project explores heart disease analysis using Python. It focuses on feature engineering, statistical exploration, and visualization to extract meaningful insights.

## Overview
In this analysis, we:

- **Feature Engineering**: Generated meaningful features from existing data.
- **Feature Selection**: Used techniques like PCA and feature importance to optimize feature sets.
- **Data Visualization**: Explored relationships between different attributes and heart disease presence.

## Dataset
- **Data Source**: `heart.csv`
- The dataset includes features such as age, sex, cholesterol levels, chest pain type, and heart disease diagnosis.

## Prerequisites
Ensure the following libraries are installed:
```bash
pip install pandas numpy matplotlib seaborn
```

## Key Steps
### 1. Data Exploration
- Load and inspect the dataset.
- Handle missing values and ensure proper data types.
- Perform descriptive statistics and data visualization.

### 2. Feature Engineering
- Created new features based on domain knowledge.
- Used PCA for dimensionality reduction.
- Analyzed feature importance to optimize model inputs.

### 3. Data Visualization
- **Heart Disease Distribution**: Pie chart and count plot.
- **Sex Distribution**: Pie chart showing gender distribution.
- **Chest Pain & Heart Disease**: Analyzed correlations between chest pain type and disease occurrence.
- **Age & Heart Disease**: Histogram showing age distribution among affected individuals.
- **Cholesterol Levels**: Violin plot illustrating cholesterol distribution.
- **Exercise-Induced Angina**: Analyzed its impact on heart disease.
- **ST Segment Analysis**: Relationship between slope of peak exercise ST segment and heart disease.

## Implementation Highlights
### Data Processing & Exploration
- Loaded dataset and checked for null values.
- Displayed dataset statistics and feature distribution.
- Visualized numerical features with histograms.

### Feature Analysis
- Examined relationships between attributes and heart disease.
- Conducted cross-tabulation analysis.
- Applied feature selection techniques.

### Visualization Techniques
- Used count plots, histograms, and pie charts for categorical data.
- Created violin plots for cholesterol distribution.
- Plotted stacked histograms for age and heart disease analysis.

## Conclusion
This project provides insights into heart disease factors through feature analysis and visualization. It helps in understanding the role of different health attributes in predicting heart disease.
