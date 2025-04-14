import streamlit as st
import requests

API_URL = "http://127.0.0.1:1000/predict"

st.set_page_config(page_title="Loan Default Predictor", page_icon="💸", layout="centered")

st.title("💸 Loan Defaulter Prediction App")
st.write("Use the sidebar to fill applicant details and predict loan default risk.")

st.sidebar.header("Applicant Information")

person_age = st.sidebar.number_input('Person Age', min_value=18, max_value=100, value=30)
person_income = st.sidebar.number_input('Person Income ($)', min_value=1000, max_value=1000000, value=50000)
person_home_ownership = st.sidebar.selectbox('Home Ownership', ['RENT', 'MORTGAGE', 'OWN', 'OTHER'])
person_emp_length = st.sidebar.number_input('Employment Length (years)', min_value=0.0, max_value=50.0, value=5.0)
loan_intent = st.sidebar.selectbox('Loan Intent', ['PERSONAL', 'EDUCATION', 'MEDICAL', 'VENTURE', 'HOMEIMPROVEMENT', 'DEBTCONSOLIDATION'])
loan_grade = st.sidebar.selectbox('Loan Grade', ['A', 'B', 'C', 'D', 'E', 'F', 'G'])
loan_amnt = st.sidebar.number_input('Loan Amount ($)', min_value=500, max_value=50000, value=15000)
loan_int_rate = st.sidebar.number_input('Loan Interest Rate (%)', min_value=2.0, max_value=30.0, value=11.5)
loan_percent_income = st.sidebar.slider('Loan Percent Income', min_value=0.0, max_value=1.0, value=0.3)
cb_person_default_on_file = st.sidebar.selectbox('Default on File', ['Y', 'N'])
cb_person_cred_hist_length = st.sidebar.number_input('Credit History Length (years)', min_value=0, max_value=50, value=5)

submit_button = st.sidebar.button('Predict')

if submit_button:
    payload = {
        "person_age": person_age,
        "person_income": person_income,
        "person_home_ownership": person_home_ownership,
        "person_emp_length": person_emp_length,
        "loan_intent": loan_intent,
        "loan_grade": loan_grade,
        "loan_amnt": loan_amnt,
        "loan_int_rate": loan_int_rate,
        "loan_percent_income": loan_percent_income,
        "cb_person_default_on_file": cb_person_default_on_file,
        "cb_person_cred_hist_length": cb_person_cred_hist_length
    }
    
    response = requests.post(API_URL, json=payload)
    
    if response.status_code == 200:
        result = response.json()
        prediction = result['loan_status_prediction']
        probability = result['default_probability']
        
        st.subheader("🔎 Prediction Results")
        st.success(f"Prediction: {'Default' if prediction == 1 else 'No Default'}")
        st.info(f"Probability of Default: {probability * 100:.2f}%")
        
        if prediction == 1:
            st.error("⚠️ Warning: High Risk of Default!")
        else:
            st.balloons()
    else:
        st.error("Error contacting the backend API. Please make sure it is running on port 1000.")
