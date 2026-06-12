import pandas as pd
import shap
import joblib
import matplotlib.pyplot as plt

# Load trained model
model = joblib.load("model.pkl")

# Load dataset
df = pd.read_csv(
    "../dataset/WA_Fn-UseC_-HR-Employee-Attrition.csv"
)

# Remove unused columns
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
from sklearn.preprocessing import LabelEncoder

for col in df.columns:

    if df[col].dtype == "object":

        le = LabelEncoder()

        df[col] = le.fit_transform(
            df[col]
        )

# Features
X = df.drop(
    "Attrition",
    axis=1
)

# SHAP Explainer
explainer = shap.TreeExplainer(
    model
)

shap_values = explainer.shap_values(X)

print("Generating SHAP Summary Plot...")

plt.figure()

shap.summary_plot(
    shap_values,
    X,
    show=False
)

plt.savefig(
    "shap_summary.png",
    bbox_inches="tight"
)

print(
    "SHAP Graph Saved Successfully"
)