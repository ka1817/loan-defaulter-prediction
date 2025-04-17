from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
import uvicorn
loaded_model = joblib.load('best_model_gb.pkl')

app = FastAPI(title='Loan Defaulter Prediction FAST API')

class Prediction(BaseModel):
    person_age: int
    person_income: float
    person_home_ownership: str
    person_emp_length: float
    loan_intent: str
    loan_grade: str
    loan_amnt: float
    loan_int_rate: float
    loan_percent_income: float
    cb_person_default_on_file: str
    cb_person_cred_hist_length: int
@app.get('/home')
def home():
    return "Loan Defaulter Prediction API"
@app.post('/predict')
def predict(data: Prediction):
    input_data = pd.DataFrame([data.dict()])
    
    prediction = loaded_model.predict(input_data)[0]
    prediction_proba = loaded_model.predict_proba(input_data)[0][1]  

    return {
        'loan_status_prediction': int(prediction),
        'default_probability': round(prediction_proba, 3)
    }

if __name__=="__main__":
    uvicorn.run(app,host='0.0.0.0',port=1000)
