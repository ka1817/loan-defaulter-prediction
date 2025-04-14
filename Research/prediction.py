import joblib
import pandas as pd 

loaded_model = joblib.load('best_model_gb.pkl')
new_data = pd.DataFrame({
    'person_age': [30],
    'person_income': [50000],
    'person_home_ownership': ['RENT'],
    'person_emp_length': [5.0],
    'loan_intent': ['PERSONAL'],
    'loan_grade': ['B'],
    'loan_amnt': [15000],
    'loan_int_rate': [11.5],
    'loan_percent_income': [0.3],
    'cb_person_default_on_file': ['N'],
    'cb_person_cred_hist_length': [5]
})
prediction = loaded_model.predict(new_data)

print(f"Predicted loan_status: {prediction[0]}")
