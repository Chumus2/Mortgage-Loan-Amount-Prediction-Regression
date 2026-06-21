import joblib
import  numpy as np

from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Annotated


app = FastAPI(
    title="Mortgage Loan Amount Predictor API",
    description="API for predicting the maximum mortgage loan amount based on financial features.",
    version="1.0.0"
)
model = joblib.load("../Machine-Learning/models/model.pkl")


class LoadInput(BaseModel):
    annual_income: Annotated[float, Field(description="Applicant's annual income in USD", example=134183)]
    interest_rate: Annotated[float, Field(description="Loan interest rate e.g. 0.05 for 5%", example=0.05)]
    credit_score: Annotated[float, Field(description="Credit score between 580 and 850", example=750)]
    existing_monthly_debt: Annotated[float, Field(description="Monthly debt payments in USD", example=1500)]
    down_payment: Annotated[float, Field(description="Down payment amount in USD", example=50000)]

class LoanOutput(BaseModel):
    max_loan_amount: Annotated[float, Field(description="Predicted maximum loan amount in USD", example=531100.66)]

@app.post("/predict", response_model=LoanOutput, summary="Predict loan amount based on financial features")
def predict(data: LoadInput):
    """
    Predict the maximum mortgage loan amount for an applicant.

    - annual_income: yearly income in USD
    - interest_rate: loan rate as decimal (0.03 - 0.08)
    - credit_score: credit score between 580 and 850
    - existing_monthly_debt: current monthly debt in USD
    - down_payment: down payment amount in USD
    """

    x = np.array([[data.annual_income, data.interest_rate,
        data.credit_score, data.existing_monthly_debt,
        data.down_payment]])

    pred = model.predict(x)

    return  {"max_loan_amount": round(pred[0], 2)}