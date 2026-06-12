import joblib
import pandas as pd

ROLE_MAPPING = {

    "Software Developer":
        "Research Scientist",

    "Frontend Developer":
        "Research Scientist",

    "Backend Developer":
        "Research Scientist",

    "Full Stack Developer":
        "Research Scientist",

    "QA Tester":
        "Laboratory Technician",

    "DevOps Engineer":
        "Research Scientist",

    "Data Analyst":
        "Research Scientist",

    "Data Engineer":
        "Research Scientist",

    "Machine Learning Engineer":
        "Research Scientist",

    "AI Engineer":
        "Research Scientist",

    "Business Analyst":
        "Manager",

    "Security Analyst":
        "Manager",

    "SOC Analyst":
        "Manager",

    "Security Engineer":
        "Manager",

    "Penetration Tester":
        "Manager",

    "Accountant":
        "Manager",

    "Financial Analyst":
        "Manager",

    "Auditor":
        "Manager",

    "Finance Manager":
        "Manager",

    "HR Executive":
        "Manager",

    "Recruiter":
        "Manager",

    "HR Manager":
        "Manager",

    "Talent Acquisition Specialist":
        "Manager",

    "Sales Executive":
        "Sales Executive",

    "Sales Manager":
        "Manager",

    "Business Development Executive":
        "Sales Executive",

    "Digital Marketing Executive":
        "Manager",

    "SEO Specialist":
        "Manager",

    "Content Strategist":
        "Manager",

    "Marketing Manager":
        "Manager",

    "Operations Executive":
        "Manager",

    "Operations Manager":
        "Manager",

    "Project Coordinator":
        "Manager",

    "Research Scientist":
        "Research Scientist",

    "Research Associate":
        "Research Scientist",

    "Innovation Engineer":
        "Research Scientist",

    "Customer Support Executive":
        "Manager",

    "Technical Support Engineer":
        "Research Scientist",

    "Support Manager":
        "Manager"
} 

model = joblib.load(
    "machine_learning/model.pkl"
)

encoders = joblib.load(
    "machine_learning/encoders.pkl"
)

DEPARTMENT_MAPPING = {

    "IT":
        "Research & Development",

    "Data Science":
        "Research & Development",

    "Cyber Security":
        "Research & Development",

    "Finance":
        "Human Resources",

    "Marketing":
        "Sales",

    "Operations":
        "Human Resources",

    "Customer Support":
        "Human Resources",

    "Human Resources":
        "Human Resources",

    "Sales":
        "Sales",

    "Research & Development":
        "Research & Development"
}

def predict_employee(
    employee_data,
    survey_data
):

    employee_data["JobRole"] = ROLE_MAPPING.get(
        employee_data["JobRole"],
        "Manager"
    )

    employee_data["Department"] = (
        DEPARTMENT_MAPPING.get(
            employee_data["Department"],
            "Human Resources"
        )
    )

    df = pd.DataFrame(
        [employee_data]
    )

    categorical_columns = [

        "BusinessTravel",

        "Department",

        "JobRole",

        "OverTime"
    ]

    for col in categorical_columns:

        df[col] = encoders[col].transform(
            df[col]
        )

    probability = model.predict_proba(
        df
    )[0][1]

    risk_score = round(
        probability * 100,
        2
    )

    # -------------------------
    # Wellness Score
    # -------------------------

    wellness_questions = [

        survey_data["manager_support"],

        survey_data["salary_satisfaction"],

        survey_data["stress_level"],

        survey_data["recognition"],

        survey_data["career_growth"],

        survey_data["training_opportunities"],

        survey_data["communication"],

        survey_data["workload"],

        survey_data["job_security"],

        survey_data["company_culture"],

        survey_data["recommend_company"]
    ]

    wellness_score = round(

        (
            sum(wellness_questions)

            /

            (len(wellness_questions) * 4)

        ) * 100,

        2
    )

    # -------------------------
    # Risk Adjustment
    # -------------------------

    adjustment = 0

    if survey_data["manager_support"] <= 2:
        adjustment += 5

    if survey_data["career_growth"] <= 2:
        adjustment += 5

    if survey_data["salary_satisfaction"] <= 2:
        adjustment += 5

    if survey_data["recognition"] <= 2:
        adjustment += 5

    if survey_data["stress_level"] <= 2:
        adjustment += 10

    if survey_data["job_security"] <= 2:
        adjustment += 5

    adjusted_risk = min(
        risk_score + adjustment,
        100
    )

    # -------------------------
    # Final Status
    # -------------------------

    if adjusted_risk >= 70:

        status = "High Risk"

    elif adjusted_risk >= 50:

        status = "Medium Risk"

    else:

        status = "Low Risk"

    return (

        risk_score,

        adjusted_risk,

        status,

        wellness_score

    )