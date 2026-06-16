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

    database_url = os.environ.get(
        "DATABASE_URL"
    )

    if database_url:

        database_url = database_url.replace(
            "postgres://",
            "postgresql://",
            1
        )

    SQLALCHEMY_DATABASE_URI = (
        database_url
        or
        "sqlite:///employee.db"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False