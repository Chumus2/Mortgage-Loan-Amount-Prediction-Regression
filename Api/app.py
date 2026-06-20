import joblib
import  numpy as np

from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()
model = joblib.load("../Machine-Learning/models/model.pkl")


class LoadInput(BaseModel):
    annual_salary: float
    interest_rate: float
    credit_score: float
    existing_monthly_debt: float
    down_payment: float

@app.post("/predict")
def predict(data: LoadInput):
    x = np.array([[data.annual_income, data.interest_rate,
        data.credit_score, data.existing_monthly_debt,
        data.down_payment]])

    pred = model.predict(x)

    return  {"max_loan_amount": round(pred[0], 2)}