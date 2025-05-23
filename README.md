# Loan Default Detection Analysis & Prediction

The goal is to predict  loan approval based on applicant financial and demographic details. 
Deplyed by interactive Streamlit web app that allows users to input data and receive instant predictions.


**I chose this dataset because it presents several challenges, it is relatively small with about 615 rows, and contains many missing values and outliers
I addressed these issues through data preprocessing and was able to achieve an accuracy of 81%, which is a strong result given the limited size of the data**

**link of the app** : https://loan-approval-analysis-and-prediction-tymsx8f4cbb8h6ykdwkwkd.streamlit.app/

## Approach & Steps:

1- Understanding the data variables: This step is important because it allows you to understand the meaning of each variable and how it might be related to the dependent variable

2- checked if the data types were correct and didn’t need changes, then looked for missing or repeated data.

3- Univariate analysis:  In this step i will go through each column and fix problems , look at the distribution of each variable and do Eda for features to understand

4- Creating new features: This step allows you to create new features that are based on the existing features. This can be helpful if you want to improve the accuracy of your model.

5- Identifying the most important variables using diff tests: This step allows you to identify the variables that have the biggest impact on the dependent variable 

6- Pipeline Building: A pipeline was created to handle preprocessing, feature engineering, and model integration, ensuring a smooth and consistent workflow for training.

7- Model Building: The model building process utilized a pipeline and cross-validation to train and test multiple models and choose best model, ensuring no data leakage and  effective model. A pipeline was established to preprocess data and integrate various models, maintaining a consistent workflow.

8- Tuning: Tuning was not done because the dataset was small, and earlier tries at tuning gave bad results most of the time.
