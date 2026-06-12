import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

from xgboost import XGBClassifier

from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

# Load Dataset
df = pd.read_csv(
    "../dataset/WA_Fn-UseC_-HR-Employee-Attrition.csv"
)

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

# Save model
joblib.dump(
    model,
    "model.pkl"
)

print("\nModel Saved")

print("\nEncoders Saved")