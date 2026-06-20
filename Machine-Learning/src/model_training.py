import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


df = pd.read_csv("../data/processed.csv")

x = df.drop(columns=["Max Loan Amount (USD)"])
y = df["Max Loan Amount (USD)"]


x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=42)

model = LinearRegression()
model.fit(x_train, y_train)


joblib.dump(model, "../models/model.pkl")