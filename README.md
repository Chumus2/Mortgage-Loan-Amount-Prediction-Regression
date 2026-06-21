# Mortgage-Loan-Amount-Prediction-Regression
Predicting the maximum mortgage loan amount a bank can offer to an applicant based on demographic and financial features using machine learning regression models.

![Preview](preview.png)

---

## Problem Statement

A bank wants to automate the process of determining the maximum mortgage loan amount for a new applicant. The model predicts the loan amount based on 5 key financial features.

---

## Features Used

| Feature | Description |
|---|---|
| Annual Income | Applicant's yearly income in USD |
| Interest Rate | Loan interest rate (e.g. 0.05 = 5%) |
| Credit Score | Applicant's credit score (580–850) |
| Existing Monthly Debt | Current monthly debt payments in USD |
| Down Payment | Initial payment amount in USD |

---

## Model Performance

| Metric | Value |
|---|---|
| Algorithm | Linear Regression |
| R² Score | 0.9502 |
| MAE | $51,858 |
| RMSE | $69,240 |

---

## Project Structure

```
Mortgage-Loan-Amount-Prediction/
├── Machine-Learning/
│   ├── data/
│   │   ├── raw.csv <-- (First uploaded dataset)
│   │   └── processed.csv <-- (Fully prepared dataset)
│   ├── models/
│   │   └── model.pkl <-- (Trained model)
│   └── notebook.ipynb
├── Api/
│   └── app.py <-- (API main file)
├── web/
│   └── app/
│       ├── app/ <-- (django project app)
│       ├── main/ <-- (main app)
│       └── manage.py 
└── README.md
```

---

## Tech Stack

- **ML:** Python, Pandas, Scikit-learn
- **Api:** FastAPI
- **Web:** Django, HTML, CSS

---

## Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/Chumus2/Mortgage-Loan-Amount-Prediction-Regression.git
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run FastAPI
```bash
cd Api
uvicorn app:app --port 8000
```

### 4. Run Django
```bash
cd web/app
python manage.py runserver 8001
```

### 5. Open in browser 
http://127.0.0.1:8001

---

## API Documentation

FastAPI auto-generates interactive docs:<br>
http://127.0.0.1:8000/docs