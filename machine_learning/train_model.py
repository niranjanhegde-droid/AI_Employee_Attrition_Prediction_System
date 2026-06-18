import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

from xgboost import XGBClassifier
import matplotlib.pyplot as plt
import seaborn as sns

from xgboost import plot_importance
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

import os

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

csv_path = os.path.join(
    BASE_DIR,
    "dataset",
    "WA_Fn-UseC_-HR-Employee-Attrition.csv"
)

df = pd.read_csv(csv_path)
# Features used in OUR SYSTEM
features = [

    "Age",

    "BusinessTravel",

    "Department",

    "DistanceFromHome",

    "Education",

    "EnvironmentSatisfaction",

    "JobRole",

    "JobSatisfaction",

    "MonthlyIncome",

    "OverTime",

    "RelationshipSatisfaction",

    "WorkLifeBalance",

    "YearsAtCompany"
]

target = "Attrition"

# Keep only required columns
df = df[features + [target]]

plt.figure(figsize=(12,8))

corr_matrix = df.corr(numeric_only=True)

sns.heatmap(
    corr_matrix,
    cmap="coolwarm",
    annot=True,
    fmt=".2f"
)

plt.title(
    "Correlation Heatmap"
)

plt.tight_layout()

plt.savefig(
    "correlation_heatmap.png"
)

plt.close()
# Encode categorical columns
label_encoders = {}

for column in df.columns:

    if df[column].dtype == "object":

        encoder = LabelEncoder()

        df[column] = encoder.fit_transform(
            df[column]
        )

        label_encoders[column] = encoder

# Save encoders
joblib.dump(
    label_encoders,
    "encoders.pkl"
)

# Features
X = df[features]

# Target
y = df[target]

# Attrition Distribution Graph

plt.figure(figsize=(6,5))

sns.countplot(x=y)

plt.title(
    "Employee Attrition Distribution"
)

plt.xlabel(
    "Attrition"
)

plt.ylabel(
    "Count"
)

plt.tight_layout()

plt.savefig(
    "attrition_distribution.png"
)

plt.close()

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Handle Imbalance
scale_weight = (
    len(y_train[y_train == 0])
    /
    len(y_train[y_train == 1])
)

# Model
model = XGBClassifier(
    n_estimators=300,
    max_depth=5,
    learning_rate=0.05,
    scale_pos_weight=scale_weight,
    random_state=42
)

model.fit(
    X_train,
    y_train
)

# Prediction
y_pred = model.predict(
    X_test
)

# Accuracy
accuracy = accuracy_score(
    y_test,
    y_pred
)

print("\nAccuracy:")
print(round(accuracy * 100, 2), "%")

print("\nClassification Report:")
print(
    classification_report(
        y_test,
        y_pred
    )
)

print("\nConfusion Matrix:")
print(
    confusion_matrix(
        y_test,
        y_pred
    )
)

cm = confusion_matrix(
    y_test,
    y_pred
)

plt.figure(figsize=(6,5))

sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    cmap="Blues"
)

plt.title(
    "Confusion Matrix"
)

plt.xlabel(
    "Predicted"
)

plt.ylabel(
    "Actual"
)

plt.tight_layout()

plt.savefig(
    "confusion_matrix.png"
)

plt.close()

plt.figure(figsize=(10,6))

plot_importance(
    model,
    max_num_features=10
)

plt.title(
    "Top Features Influencing Attrition"
)

plt.tight_layout()

plt.savefig(
    "feature_importance.png"
)

plt.close()

# Save model
joblib.dump(
    model,
    "model.pkl"
)

print("\nModel Saved")

print("\nEncoders Saved")