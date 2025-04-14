import sys
import os

# Add the root directory to sys.path so that the import from main works
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_home():
    """Test the /home GET endpoint."""
    response = client.get("/home")
    assert response.status_code == 200
    assert response.json() == "Loan Defaulter Prediction"

def test_predict():
    """Test the /predict POST endpoint."""
    payload = {
        "person_age": 35,
        "person_income": 55000,
        "person_home_ownership": "RENT",
        "person_emp_length": 5.0,
        "loan_intent": "EDUCATION",
        "loan_grade": "B",
        "loan_amnt": 12000.0,
        "loan_int_rate": 11.5,
        "loan_percent_income": 0.2,
        "cb_person_default_on_file": "N",
        "cb_person_cred_hist_length": 5
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    assert "loan_status_prediction" in response.json()
    assert "default_probability" in response.json()
