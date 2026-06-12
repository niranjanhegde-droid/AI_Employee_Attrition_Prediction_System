from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    PasswordField,
    SubmitField
)

from wtforms.validators import (
    DataRequired,
    Email,
    EqualTo
)

from wtforms.validators import (
    DataRequired,
    Email,
    Length,
    EqualTo
)
from wtforms import RadioField 

class RegisterForm(FlaskForm):

    name = StringField(
        "Full Name",
        validators=[DataRequired()]
    )

    email = StringField(

        "Email",

        validators=[

            DataRequired(),

            Email(
                message=
                "Please enter a valid email address."
            )
        ]
    )

    password = PasswordField(
        "Password",
        validators=[DataRequired()]
    )

    confirm_password = PasswordField(
        "Confirm Password",
        validators=[
            DataRequired(),
            EqualTo('password')
        ]
    )

    submit = SubmitField("Register")


class LoginForm(FlaskForm):

    email = StringField(

    "Email",

    validators=[

        DataRequired(),

        Email(
            message=
            "Please enter a valid email address."
        )
    ]
)

    password = PasswordField(
        "Password",
        validators=[DataRequired()]
    )

    submit = SubmitField("Login")

from wtforms import IntegerField
from wtforms import SelectField


class EmployeeProfileForm(FlaskForm):

    age = IntegerField(
        "Age",
        validators=[DataRequired()]
    )

    gender = SelectField(
        "Gender",
        choices=[
            ("Male", "Male"),
            ("Female", "Female")
        ]
    )

    department = SelectField(
    "Department",
    choices=[
        ("IT", "IT"),
        ("Data Science", "Data Science"),
        ("Cyber Security", "Cyber Security"),
        ("Finance", "Finance"),
        ("Human Resources", "Human Resources"),
        ("Sales", "Sales"),
        ("Marketing", "Marketing"),
        ("Operations", "Operations"),
        ("Research & Development", "Research & Development"),
        ("Customer Support", "Customer Support")
    ]
)

    job_role = SelectField(
    "Job Role",
    choices=[
        ("Software Developer","Software Developer")
    ],
    validate_choice=False
)

    monthly_income = IntegerField(
        "Monthly Income",
        validators=[DataRequired()]
    )

    overtime = SelectField(
        "OverTime",
        choices=[
            ("Yes", "Yes"),
            ("No", "No")
        ]
    )

    years_at_company = IntegerField(
        "Years At Company",
        validators=[DataRequired()]
    )

    distance_from_home = IntegerField(
        "Distance From Home",
        validators=[DataRequired()]
    )

    education = SelectField(
        "Education",
        choices=[
            (1, "Below College"),
            (2, "College"),
            (3, "Bachelor"),
            (4, "Master"),
            (5, "Doctor")
        ],
        coerce=int
    )

    business_travel = SelectField(
        "Business Travel",
        choices=[
            ("Travel_Rarely",
             "Travel Rarely"),

            ("Travel_Frequently",
             "Travel Frequently"),

            ("Non-Travel",
             "Non Travel")
        ]
    )

    submit = SubmitField(
        "Save Profile"
    )

class SurveyForm(FlaskForm):

    job_satisfaction = SelectField(
        "How satisfied are you with your job?",
        choices=[
                    ("", "Select Option"),

            (1, "Very Dissatisfied"),
            (2, "Dissatisfied"),
            (3, "Satisfied"),
            (4, "Very Satisfied")
        ],
validators=[DataRequired()]
    )

    environment_satisfaction = SelectField(
        "How satisfied are you with your work environment?",
        choices=[
                ("", "Select Option"),

            (1, "Very Dissatisfied"),
            (2, "Dissatisfied"),
            (3, "Satisfied"),
            (4, "Very Satisfied")
        ],
validators=[DataRequired()]    )

    work_life_balance = SelectField(
        "How would you rate your work-life balance?",
        choices=[
            ("", "Select Option"),

            (1, "Poor"),
            (2, "Average"),
            (3, "Good"),
            (4, "Excellent")
        ],
validators=[DataRequired()]    )

    relationship_satisfaction = SelectField(
        "How satisfied are you with your team relationships?",
        choices=[
            ("", "Select Option"),

            (1, "Very Dissatisfied"),
            (2, "Dissatisfied"),
            (3, "Satisfied"),
            (4, "Very Satisfied")
        ],
validators=[DataRequired()]    )

    manager_support = SelectField(
        "How supportive is your manager?",
        choices=[
            ("", "Select Option"),

            (1, "Very Poor"),
            (2, "Poor"),
            (3, "Good"),
            (4, "Excellent")
        ],
validators=[DataRequired()]    )

    salary_satisfaction = SelectField(
        "How satisfied are you with your salary?",
        choices=[

            ("", "Select Option"),

            (1, "Very Dissatisfied"),
            (2, "Dissatisfied"),
            (3, "Satisfied"),
            (4, "Very Satisfied")
        ],
validators=[DataRequired()]    )

    stress_level = SelectField(
        "How would you rate your stress level?",
        choices=[
            ("", "Select Option"),

            (1, "Very High"),
            (2, "High"),
            (3, "Moderate"),
            (4, "Low")
        ],
validators=[DataRequired()]    )

    recognition = SelectField(
        "Do you feel recognized for your work?",
        choices=[
            ("", "Select Option"),

            (1, "Never"),
            (2, "Rarely"),
            (3, "Often"),
            (4, "Always")
        ],
validators=[DataRequired()]    )

    career_growth = SelectField(
        "How do you rate career growth opportunities?",
        choices=[
            ("", "Select Option"),

            (1, "Very Poor"),
            (2, "Poor"),
            (3, "Good"),
            (4, "Excellent")
        ],
validators=[DataRequired()]    )

    training_opportunities = SelectField(
        "How would you rate training opportunities?",
        choices=[
            ("", "Select Option"),

            (1, "Very Poor"),
            (2, "Poor"),
            (3, "Good"),
            (4, "Excellent")
        ],
validators=[DataRequired()]    )

    communication = SelectField(
        "How effective is communication in your organization?",
        choices=[
            ("", "Select Option"),

            (1, "Very Poor"),
            (2, "Poor"),
            (3, "Good"),
            (4, "Excellent")
        ],
validators=[DataRequired()]    )

    workload = SelectField(
        "How manageable is your workload?",
        choices=[
            ("", "Select Option"),

            (1, "Very Difficult"),
            (2, "Difficult"),
            (3, "Manageable"),
            (4, "Very Manageable")
        ],
validators=[DataRequired()]    )

    job_security = SelectField(
        "How secure do you feel in your current position?",
        choices=[
            ("", "Select Option"),

            (1, "Very Insecure"),
            (2, "Insecure"),
            (3, "Secure"),
            (4, "Very Secure")
        ],
validators=[DataRequired()]    )

    company_culture = SelectField(
        "How satisfied are you with company culture?",
        choices=[
            ("", "Select Option"),

            (1, "Very Dissatisfied"),
            (2, "Dissatisfied"),
            (3, "Satisfied"),
            (4, "Very Satisfied")
        ],
validators=[DataRequired()]    )

    recommend_company = SelectField(
        "Would you recommend this company to others?",
        choices=[
            ("", "Select Option"),

            (1, "Definitely No"),
            (2, "Probably No"),
            (3, "Probably Yes"),
            (4, "Definitely Yes")
        ],
validators=[DataRequired()]    )

    submit = SubmitField(
        "Submit Survey"
    )

class AdminRegisterForm(FlaskForm):

    name = StringField(
        "Full Name",
        validators=[DataRequired()]
    )
    email = StringField(

        "Email",

        validators=[

            DataRequired(),

            Email(
                message=
                "Please enter a valid admin email."
            )
        ]
    )

    password = PasswordField(
        "Password",
        validators=[DataRequired()]
    )

    secret_key = StringField(
        "Admin Secret Key",
        validators=[DataRequired()]
    )

    submit = SubmitField(
        "Register Admin"
    )