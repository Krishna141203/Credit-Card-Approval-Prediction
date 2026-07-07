import streamlit as st
import pandas as pd
import pickle

# Load trained model
model = pickle.load(open("model.pkl", "rb"))

st.title("Credit Card Approval Prediction")

st.write("Enter customer details")

Age = st.number_input("Age", min_value=18, max_value=80, value=30)

Gender = st.selectbox(
    "Gender",
    ["Female", "Male"]
)

Income = st.number_input(
    "Income",
    min_value=10000,
    max_value=100000,
    value=50000
)

Education = st.selectbox(
    "Education",
    ["Graduate", "Postgraduate", "Undergraduate"]
)

Employment = st.selectbox(
    "Employment",
    ["Unemployed", "Salaried", "Self_Employed"]
)

Marital_Status = st.selectbox(
    "Marital Status",
    ["Single", "Married"]
)

Loan_Amount = st.number_input(
    "Loan Amount",
    min_value=1000,
    max_value=50000,
    value=10000
)

Credit_History = st.selectbox(
    "Credit History",
    [0, 1]
)

Existing_Loan = st.selectbox(
    "Existing Loan",
    [0, 1]
)


if st.button("Predict"):

    input_data = pd.DataFrame({
        "Age": [Age],
        "Gender": [1 if Gender=="Male" else 0],
        "Income": [Income],
        "Education": [0 if Education=="Undergraduate" else 1],
        "Employment": [1 if Employment=="Salaried" else 0],
        "Marital_Status": [1 if Marital_Status=="Married" else 0],
        "Loan_Amount": [Loan_Amount],
        "Credit_History": [Credit_History],
        "Existing_Loan": [Existing_Loan]
    })


    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("Credit Card Approved ✅")
    else:
        st.error("Credit Card Rejected ❌")