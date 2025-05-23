import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load model
with open('/Users/mohammedmahmood/Desktop/Data projects/Data science/Loan Default Detection Prediction  Main/Loan_Approval_analysis_and_prediction.sav', "rb") as file:
    model = pickle.load(file)
    
st.title(" Loan Approval Prediction App")
st.write("Provide the necessary details to predict whether a loan will be approved")

# User Inputs
applicant_income = st.slider("Applicant Income", min_value=0.0, value=5000.0)
coapplicant_income = st.slider("Coapplicant Income", min_value=0.0, value=1500.0)
# st.markdowen
total_income = applicant_income + coapplicant_income
st.metric("Total Income =  applicant income + coapplicant income ", f"{total_income:.2f}")

loan_amount = st.slider("Loan Amount (in thousands)", min_value=0.0, value=150.0)
income_to_loan_ratio = total_income / (loan_amount * 1000) if loan_amount > 0 else 0

loan_term = st.slider("Loan Amount Term (in days)", min_value=1.0, value=360.0)
st.subheader(" Auto Calculated features")
loan_monthly_paid = loan_amount * 1000 / loan_term
st.metric("Monthly Loan Payment = loan amount * 1000 / loan term", f"{loan_monthly_paid:.2f}")
st.metric("Income to Loan Ratio = total income / (loan amount * 1000)", f"{income_to_loan_ratio:.2f}")

income_after_loan = total_income - loan_monthly_paid
st.metric("Income After Loan = total income - loan monthly paid", f"{income_after_loan:.2f}")

credit_history = st.selectbox("Credit History", options=[1.0, 0.0], index=0)
married = st.selectbox("Married", options=["Yes", "No"])
property_area = st.selectbox("Property Area", options=["Urban", "Rural", "Semiurban"])

# Feature Engineering

# Log Transformations 
log_applicant_income = np.log(applicant_income )
log_loan_amount = np.log(loan_amount )
log_total_income = np.log(total_income )
log_loan_monthly_paid = np.log(loan_monthly_paid )
log_income_after_loan = np.log(max(income_after_loan, 0) )


if st.button("Predict Loan Approval"):
    input_data = pd.DataFrame([{
        'ApplicantIncome': applicant_income,
        'CoapplicantIncome': coapplicant_income,
        'LoanAmount': loan_amount,
        'Loan_Amount_Term': loan_term,
        'Credit_History': credit_history,
        'Married': married,
        'Property_Area': property_area,
        'Total_Income': total_income,
        'Loan_Monthly_Paid': loan_monthly_paid,
        'Income_to_LoanRatio': income_to_loan_ratio,
        'log_ApplicantIncome': log_applicant_income,
        'log_LoanAmount': log_loan_amount,
        'log_Total_Income': log_total_income,
        'log_Loan_Monthly_Paid': log_loan_monthly_paid,
        'log_Income_After_Loan': log_income_after_loan,
    }])

    try:
        prediction = model.predict(input_data)
        if prediction[0] == 1:
            st.success("✅ Loan is likely to be APPROVED based on information.")
        else:
            st.error("❌ Loan is likely to be REJECTED based on his information.")
    except Exception as e:
        st.error(f"🚨 Error making prediction: {e}")
