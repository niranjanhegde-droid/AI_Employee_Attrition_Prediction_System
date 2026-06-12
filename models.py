from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime

db = SQLAlchemy()


# =========================
# USER TABLE
# =========================

class User(UserMixin, db.Model):

    __tablename__ = "users"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(100),
        nullable=False
    )

    email = db.Column(
        db.String(120),
        unique=True,
        nullable=False
    )

    password = db.Column(
        db.String(255),
        nullable=False
    )

    role = db.Column(
        db.String(20),
        default="employee"
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    employee = db.relationship(
        "Employee",
        backref="user",
        uselist=False
    )


# =========================
# EMPLOYEE TABLE
# =========================

class Employee(db.Model):

    __tablename__ = "employees"

    employee_id = db.Column(
        db.String(20),
        primary_key=True
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id")
    )

    age = db.Column(db.Integer)

    gender = db.Column(
        db.String(20)
    )

    department = db.Column(
        db.String(100)
    )

    job_role = db.Column(
        db.String(100)
    )

    monthly_income = db.Column(
        db.Integer
    )

    overtime = db.Column(
        db.String(20)
    )

    years_at_company = db.Column(
        db.Integer
    )

    distance_from_home = db.Column(
        db.Integer
    )

    education = db.Column(
        db.Integer
    )

    business_travel = db.Column(
        db.String(100)
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )


# =========================
# SURVEY TABLE
# =========================

class Survey(db.Model):

    __tablename__ = "surveys"

    survey_id = db.Column(
        db.Integer,
        primary_key=True
    )

    employee_id = db.Column(
        db.String(20),
        db.ForeignKey(
            "employees.employee_id"
        )
    )

    # Existing Questions

    job_satisfaction = db.Column(
        db.Integer
    )

    environment_satisfaction = db.Column(
        db.Integer
    )

    work_life_balance = db.Column(
        db.Integer
    )

    relationship_satisfaction = db.Column(
        db.Integer
    )

    # New Questions

    manager_support = db.Column(
        db.Integer
    )

    salary_satisfaction = db.Column(
        db.Integer
    )

    stress_level = db.Column(
        db.Integer
    )

    recognition = db.Column(
        db.Integer
    )

    career_growth = db.Column(
        db.Integer
    )

    training_opportunities = db.Column(
        db.Integer
    )

    communication = db.Column(
        db.Integer
    )

    workload = db.Column(
        db.Integer
    )

    job_security = db.Column(
        db.Integer
    )

    company_culture = db.Column(
        db.Integer
    )

    recommend_company = db.Column(
        db.Integer
    )

    submitted_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )


# =========================
# PREDICTION TABLE
# =========================

class Prediction(db.Model):

    __tablename__ = "predictions"

    prediction_id = db.Column(
        db.Integer,
        primary_key=True
    )

    employee_id = db.Column(
        db.String(20),
        db.ForeignKey(
            "employees.employee_id"
        )
    )

    risk_score = db.Column(
        db.Float
    )

    prediction_result = db.Column(
        db.String(50)
    )

    recommendation = db.Column(
        db.Text
    )

    prediction_date = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )