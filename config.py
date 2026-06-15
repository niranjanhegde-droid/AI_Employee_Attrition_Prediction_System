import os

BASE_DIR = os.path.abspath(
    os.path.dirname(__file__)
)

class Config:

    SECRET_KEY = os.environ.get(
        "SECRET_KEY",
        "employee_attrition_secret_key"
    )

    ADMIN_SECRET = os.environ.get(
        "ADMIN_SECRET",
        "ADMIN2026"
    )

    SQLALCHEMY_DATABASE_URI = "sqlite:///employee.db"

    SQLALCHEMY_TRACK_MODIFICATIONS = False