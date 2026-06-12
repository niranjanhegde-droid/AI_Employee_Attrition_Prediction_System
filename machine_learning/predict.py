import joblib
import pandas as pd

model = joblib.load(
    "model.pkl"
)

def predict_employee(employee_data):

    df = pd.DataFrame(
        [employee_data]
    )

    probability = model.predict_proba(
        df
    )[0][1]

    prediction = model.predict(
        df
    )[0]

    risk_percent = round(
        probability * 100,
        2
    )

    status = (
        "High Risk"
        if prediction == 1
        else "Low Risk"
    )

    return {
        "risk_score": risk_percent,
        "status": status
    }