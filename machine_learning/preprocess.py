import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load Dataset
df = pd.read_csv(
    "../dataset/WA_Fn-UseC_-HR-Employee-Attrition.csv"
)

print("\nDataset Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

# Drop useless columns
df.drop(
    columns=[
        "EmployeeCount",
        "EmployeeNumber",
        "Over18",
        "StandardHours"
    ],
    inplace=True
)

# Encode categorical columns
label_encoders = {}

for column in df.columns:

    if df[column].dtype == "object":

        le = LabelEncoder()

        df[column] = le.fit_transform(
            df[column]
        )

        label_encoders[column] = le

print("\nPreprocessing Completed")

print(df.head())