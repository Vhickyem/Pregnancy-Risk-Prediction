# 🍼Pregnancy-Risk-Prediction

## 📌Overview  
This project uses machine learning to predict pregnancy-related risks based on patient data. The goal is to support healthcare professionals in identifying high-risk pregnancies early for timely intervention and improved health outcomes.  
## 🔍Problem Statement  
We want to build a machine learning model which takes in pregnant patients' clinical data and helps healthcare professionals' decision as to whether the pregnancy is high-risk or low-risk, which will lead to better decision making and also help with making targeted treatments, thereby improving patient outcome.  
## 📊Dataset  
* Source: Real patient data from a general hospital in bangladesh
* Rows: 1,205 patients
* Features: Age, Systolic BP, Diastolic BP, Blood Sugar level, Body Temperature, Body Mass Index (BMI), Previous complications, Preexisting diabetes, Gestational Diabetes, Mental Health, and Heart Rate.
* Target: Risk Level (Low / High)
## 🧠Methods
### Preprocessing
* Invalid and null values were removed
* Leaky columns like Gestational diabetes were removed
* Multicollinear columns like Diastolic and Systolic BP were dropped after using them to form a new column "BP Ratio"
* Feature Scaling
* Encoding categorical variables
### Exploratory Data Analysis
* Summary Statistics
* Univariate and Bivariate Analysis
* Correlation
* Statistical Analysis
### Modelling  
Several models were applied using an AutoML model called **PyCaret**. The following models were applied:
* Logistic Regression
* Naive Bayes Classifier
* Decision Tree Classifier
* K-Neighbors Classifier
* Random Forest Classifier
* Models were evaluated using Accuracy, AUC score, Recall, Precision, and F1 score.  

## 📦Install dependencies:
```!pip install -r requirements.txt```
