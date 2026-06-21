import requests
from django.shortcuts import render, redirect
from django.contrib import  messages


def check_inputs(request, field : dict):
    valid = True

    for name, value in field.items():
        if value is None or value.strip() == "":
            messages.error(request, f"{name} is required.")
            valid = False
        else:
            try:
                float(value)
            except ValueError:
                messages.error(request, f"{name} must be a number.")
                valid = False

    return valid

def main(request):
    if request.method == "POST":
        annual_income = request.POST.get("annual_income")
        interest_rate = request.POST.get("interest_rate")
        credit_score = request.POST.get("credit_score")
        monthly_debt = request.POST.get("monthly_debt")
        down_payment = request.POST.get("down_payment")

        fields = {
            "annual_income": annual_income,
            "interest_rate": interest_rate,
            "credit_score": credit_score,
            "monthly_debt": monthly_debt,
            "down_payment": down_payment
        }

        if not check_inputs(request, fields):
            return render(request, "main/main.html")

        response = requests.post("http://127.0.0.1:8000/predict", json={
            "annual_income": float(annual_income),
            "interest_rate": float(interest_rate),
            "credit_score": float(credit_score),
            "existing_monthly_debt": float(monthly_debt),
            "down_payment": float(down_payment)
        })

        result = f"{response.json()["max_loan_amount"]:,.2f}"
        return  render(request, "main/main.html", {"result": result})

    return render(request, "main/main.html")