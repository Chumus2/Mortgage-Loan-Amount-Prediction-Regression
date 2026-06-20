import pandas as pd


df = pd.read_csv('../data/raw.csv')


df["Gender"] = df["Gender"].map({
    "Male": 0, "Female": 1
})

df["Married"] = df["Married"].map({
    "Yes": 1, "No": 0
})

df = pd.get_dummies(df, columns=["Job", "Education", "Area"])


df.to_csv('../data/processed.csv', index=False)