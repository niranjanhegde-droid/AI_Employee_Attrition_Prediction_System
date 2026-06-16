from flask import Flask
from flask import render_template
from flask import redirect
from flask import url_for
from flask import flash
from flask import request

from flask_login import (
    LoginManager,
    login_user,
    logout_user,
    login_required
)
from models import Employee
from flask_bcrypt import Bcrypt

from forms import (
    EmployeeProfileForm,
    AdminRegisterForm
)

from config import Config
from flask_login import current_user
from forms import SurveyForm
from models import (
    db,
    User,
    Employee,
    Survey,
    Prediction,
    DeletedEmployee
)

from models import Employee

from forms import RegisterForm
from forms import LoginForm
from forms import EmployeeProfileForm

from models import Survey
from models import Prediction

from machine_learning.flask_predict import (
    predict_employee
)

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)

from reportlab.lib import colors

from flask import send_file

from models import DeletedEmployee

app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)

bcrypt = Bcrypt(app)

login_manager = LoginManager(app)

login_manager.login_view = "login"


@login_manager.user_loader
def load_user(user_id):
    return db.session.get(
    User,
    int(user_id)
)


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("home.html")



@app.route("/register", methods=["GET", "POST"])
def register():

    form = RegisterForm()

    if form.validate_on_submit():

        existing_user = User.query.filter_by(
            email=form.email.data
        ).first()

        if existing_user:

            flash(
                "Email already registered. Please login.",
                "danger"
            )

            return redirect(
                url_for("register")
            )

        hashed_password = bcrypt.generate_password_hash(
            form.password.data
        ).decode("utf-8")

        user = User(
            name=form.name.data,
            email=form.email.data,
            password=hashed_password,
            role="employee"
        )

        db.session.add(user)
        db.session.commit()

        flash(
            "Registration Successful!",
            "success"
        )

        return redirect(
            url_for("login")
        )

    return render_template(
        "auth/register.html",
        form=form
    )


@app.route("/login", methods=["GET", "POST"])
def login():

    if current_user.is_authenticated:

        if current_user.role == "admin":

            return redirect(
                url_for("admin_dashboard")
            )

        else:

            return redirect(
                url_for("employee_dashboard")
            )

    form = LoginForm()

    if form.validate_on_submit():

        user = User.query.filter_by(
            email=form.email.data
        ).first()

        if user and bcrypt.check_password_hash(
            user.password,
            form.password.data
        ):

            login_user(user)

            if user.role == "admin":

                return redirect(
                    url_for("admin_dashboard")
                )

            else:

                employee = Employee.query.filter_by(
                    user_id=user.id
                ).first()

                if employee:

                    return redirect(
                        url_for("employee_dashboard")
                    )

                else:

                    return redirect(
                        url_for("employee_profile")
                    )

        flash(
            "Invalid Credentials",
            "danger"
        )

    return render_template(
        "auth/login.html",
        form=form
    )

@app.route("/logout")
@login_required
def logout():

    logout_user()

    return redirect(
        url_for("home")
    )
@app.route(
    "/employee/profile",
    methods=["GET", "POST"]
)
@login_required
def employee_profile():

    form = EmployeeProfileForm()

    if form.validate_on_submit():

        existing = Employee.query.filter_by(
            user_id=current_user.id
        ).first()

        if existing:

            flash(
                "Profile already exists.",
                "warning"
            )

            return redirect(
                url_for("employee_dashboard")
            )

        employee_count = Employee.query.count()

        employee_id = (
            f"EMP{employee_count+1:03d}"
        )

        employee = Employee(

            employee_id=employee_id,

            user_id=current_user.id,

            age=form.age.data,

            gender=form.gender.data,

            department=form.department.data,

            job_role=form.job_role.data,

            monthly_income=form.monthly_income.data,

            overtime=form.overtime.data,

            years_at_company=form.years_at_company.data,

            distance_from_home=form.distance_from_home.data,

            education=form.education.data,

            business_travel=form.business_travel.data
        )

        db.session.add(employee)

        db.session.commit()

        flash(
            "Profile Saved Successfully!",
            "success"
        )

        return redirect(
            url_for("employee_survey")
        )

    return render_template(
        "employee/profile.html",
        form=form
    )

@app.route(
    "/employee/survey",
    methods=["GET", "POST"]
)
@login_required
def employee_survey():

    form = SurveyForm()

    employee = Employee.query.filter_by(
        user_id=current_user.id
    ).first()

    if not employee:

        flash(
            "Please complete profile first.",
            "warning"
        )

        return redirect(
            url_for("employee_profile")
        )

    if form.validate_on_submit():

        existing_survey = Survey.query.filter_by(
            employee_id=employee.employee_id
        ).first()

        if existing_survey:

            existing_survey.job_satisfaction = form.job_satisfaction.data
            existing_survey.environment_satisfaction = form.environment_satisfaction.data
            existing_survey.work_life_balance = form.work_life_balance.data
            existing_survey.relationship_satisfaction = form.relationship_satisfaction.data

            existing_survey.manager_support = form.manager_support.data
            existing_survey.salary_satisfaction = form.salary_satisfaction.data
            existing_survey.stress_level = form.stress_level.data
            existing_survey.recognition = form.recognition.data
            existing_survey.career_growth = form.career_growth.data
            existing_survey.training_opportunities = form.training_opportunities.data
            existing_survey.communication = form.communication.data
            existing_survey.workload = form.workload.data
            existing_survey.job_security = form.job_security.data
            existing_survey.company_culture = form.company_culture.data
            existing_survey.recommend_company = form.recommend_company.data

        else:

            survey = Survey(

                employee_id=employee.employee_id,

                job_satisfaction=form.job_satisfaction.data,

                environment_satisfaction=form.environment_satisfaction.data,

                work_life_balance=form.work_life_balance.data,

                relationship_satisfaction=form.relationship_satisfaction.data,

                manager_support=form.manager_support.data,

                salary_satisfaction=form.salary_satisfaction.data,

                stress_level=form.stress_level.data,

                recognition=form.recognition.data,

                career_growth=form.career_growth.data,

                training_opportunities=form.training_opportunities.data,

                communication=form.communication.data,

                workload=form.workload.data,

                job_security=form.job_security.data,

                company_culture=form.company_culture.data,

                recommend_company=form.recommend_company.data
            )

            db.session.add(survey)

        db.session.commit()

        flash(
            "Survey Submitted Successfully!",
            "success"
        )

        return redirect(
            url_for("employee_dashboard")
        )

    return render_template(
        "employee/survey.html",
        form=form
    )

@app.route("/admin/dashboard")
@login_required
def admin_dashboard():

    if current_user.role != "admin":

        return "Access Denied"

    total_employees = Employee.query.count()

    total_predictions = Prediction.query.count()

    high_risk = Prediction.query.filter(
        Prediction.risk_score >= 70
    ).count()

    low_risk = Prediction.query.filter(
        Prediction.risk_score < 70
    ).count()

    total_admins = User.query.filter_by(
        role="admin"
    ).count()

    deleted_employees = DeletedEmployee.query.count()

    departments = [

        "IT",

        "Finance",

        "Sales",

        "Human Resources",

        "Marketing",

        "Operations",

        "Data Science",

        "Cyber Security",

        "Research & Development",

        "Customer Support"
    ]

    department_stats = []

    for dept in departments:

        employees = Employee.query.filter_by(
            department=dept
        ).all()

        employee_count = len(employees)

        risk_scores = []

        for emp in employees:

            prediction = Prediction.query.filter_by(
                employee_id=emp.employee_id
            ).order_by(
                Prediction.prediction_date.desc()
            ).first()

            if prediction:

                risk_scores.append(
                    prediction.risk_score
                )

        avg_risk = 0

        if risk_scores:

            avg_risk = round(
                sum(risk_scores)
                /
                len(risk_scores),
                2
            )

        department_stats.append({

            "department": dept,

            "employee_count": employee_count,

            "avg_risk": avg_risk
        })

    return render_template(

    "admin/dashboard.html",

    total_employees=total_employees,

    total_predictions=total_predictions,

    high_risk=high_risk,

    low_risk=low_risk,

    total_admins=total_admins,

    deleted_employees=deleted_employees,

    department_stats=department_stats
)

@app.route("/admin/employees")
@login_required
def admin_employees():

    if current_user.role != "admin":

        return "Access Denied"

    employees = Employee.query.all()

    return render_template(
        "admin/employees.html",
        employees=employees
    )

@app.route("/admin/predict/<employee_id>")
@login_required
def admin_predict(employee_id):

    if current_user.role != "admin":

        return "Access Denied"

    employee = Employee.query.filter_by(
        employee_id=employee_id
    ).first()

    survey = Survey.query.filter_by(
        employee_id=employee_id
    ).first()

    if not survey:

        flash(
            "Employee has not completed the survey yet.",
            "warning"
        )

        return redirect(
            url_for("admin_employees")
        )

    survey_data = {

        "manager_support":
            survey.manager_support,

        "salary_satisfaction":
            survey.salary_satisfaction,

        "stress_level":
            survey.stress_level,

        "recognition":
            survey.recognition,

        "career_growth":
            survey.career_growth,

        "training_opportunities":
            survey.training_opportunities,

        "communication":
            survey.communication,

        "workload":
            survey.workload,

        "job_security":
            survey.job_security,

        "company_culture":
            survey.company_culture,

        "recommend_company":
            survey.recommend_company
    }
    drivers = []

    if survey.manager_support <= 2:

        drivers.append(
            ("Manager Support", 25)
        )

    if survey.stress_level <= 2:

        drivers.append(
            ("Stress Level", 35)
        )

    if survey.career_growth <= 2:

        drivers.append(
            ("Career Growth", 18)
        )

    if survey.salary_satisfaction <= 2:

        drivers.append(
            ("Salary Satisfaction", 12)
        )

    if survey.recognition <= 2:

        drivers.append(
            ("Recognition", 10)
        )

    drivers.sort(
        key=lambda x: x[1],
        reverse=True
    )
    if not employee:
        return "Employee Record Not Found"

    employee_data = {

    "Age": employee.age,

    "BusinessTravel": employee.business_travel,

    "Department": employee.department,

    "DistanceFromHome": employee.distance_from_home,

    "Education": employee.education,

    "EnvironmentSatisfaction":
        survey.environment_satisfaction,

    "JobRole": employee.job_role,

    "JobSatisfaction":
        survey.job_satisfaction,

    "MonthlyIncome":
        employee.monthly_income,

    "OverTime":
        employee.overtime,

    "RelationshipSatisfaction":
        survey.relationship_satisfaction,

    "WorkLifeBalance":
        survey.work_life_balance,

    "YearsAtCompany":
        employee.years_at_company
}

    risk_score, adjusted_risk, status, wellness_score = (
    predict_employee(
        employee_data,
        survey_data
    )
)

    recommendations = []

    if survey.manager_support <= 2:
        recommendations.append(
            "Improve manager support"
        )

    if survey.stress_level <= 2:
        recommendations.append(
            "Reduce workload and stress"
        )

    if survey.career_growth <= 2:
        recommendations.append(
            "Discuss career growth opportunities"
        )

    if survey.salary_satisfaction <= 2:
        recommendations.append(
            "Review compensation package"
        )

    if survey.recognition <= 2:
        recommendations.append(
            "Increase employee recognition"
        )

    if survey.job_security <= 2:
        recommendations.append(
            "Address job security concerns"
        )

    if len(recommendations) == 0:

        recommendations.append(
            "Employee appears stable"
        )

    recommendation = " | ".join(
        recommendations
    )
    persona = "Stable Performer"

    persona_reason = []

        # Burnout

    if (

            survey.stress_level <= 2

            and

            survey.work_life_balance <= 2

        ):

            persona = "Burnout Candidate"

            persona_reason = [

                "High Stress",

                "Poor Work-Life Balance"
            ]

        # Career Growth

    elif (

            survey.career_growth <= 2

        ):

            persona = "Career Seeker"

            persona_reason = [

                "Limited Career Growth",

                "Promotion Dissatisfaction"
            ]

        # Salary

    elif (

            survey.salary_satisfaction <= 2

        ):

            persona = "Salary Sensitive"

            persona_reason = [

                "Salary Dissatisfaction"
            ]

        # Manager

    elif (

            survey.manager_support <= 2

        ):

            persona = "Manager Conflict Risk"

            persona_reason = [

                "Poor Manager Support"
            ]

        # Recognition

    elif (

            survey.recognition <= 2

        ):

            persona = "Disengaged Employee"

            persona_reason = [

                "Low Recognition"
            ]

    risk_factors = []

    if survey.stress_level <= 2:
        risk_factors.append(
            "High Stress Level"
        )

    if survey.manager_support <= 2:
        risk_factors.append(
            "Poor Manager Support"
        )

    if survey.career_growth <= 2:
        risk_factors.append(
            "Limited Career Growth"
        )

    if survey.salary_satisfaction <= 2:
        risk_factors.append(
            "Salary Dissatisfaction"
        )

    if survey.recognition <= 2:
        risk_factors.append(
            "Lack of Recognition"
        )

    if survey.job_security <= 2:
        risk_factors.append(
            "Job Security Concerns"
        )

    if len(risk_factors) == 0:

        risk_factors.append(
            "No Major Risk Factors Detected"
        )

    prediction_record = Prediction(

        employee_id=employee_id,

        risk_score=adjusted_risk,

        prediction_result=status,

        recommendation=recommendation
    )

    db.session.add(
        prediction_record
    )

    db.session.commit()

    return render_template(

        "admin/predict.html",

        employee=employee,

        risk_score=risk_score,

        adjusted_risk=adjusted_risk,

        wellness_score=wellness_score,

        status=status,

        recommendation=recommendation,

        risk_factors=risk_factors,

        persona=persona,

        persona_reason=persona_reason,

        driver_ranking=drivers
    )
@app.route(
    "/admin/login",
    methods=["GET", "POST"]
)
def admin_login():

    form = LoginForm()

    if form.validate_on_submit():

        user = User.query.filter_by(
            email=form.email.data,
            role="admin"
        ).first()

        if user and bcrypt.check_password_hash(
            user.password,
            form.password.data
        ):

            login_user(user)

            return redirect(
                url_for("admin_dashboard")
            )

        flash(
            "Invalid Admin Credentials",
            "danger"
        )

    return render_template(
        "auth/admin_login.html",
        form=form
    )

@app.route("/employee/dashboard")
@login_required
def employee_dashboard():

    if current_user.role != "employee":

        return "Access Denied"

    employee = Employee.query.filter_by(
        user_id=current_user.id
    ).first()

    if not employee:

        return redirect(
            url_for("employee_profile")
        )

    survey = Survey.query.filter_by(
        employee_id=employee.employee_id
    ).first()

    if not survey:

        flash(
            "Please complete the survey first.",
            "warning"
        )

        return redirect(
            url_for("employee_survey")
        )

    return render_template(
        "employee/dashboard.html",
        employee=employee
    )

@app.route(
    "/admin/report/<employee_id>"
)
@login_required
def generate_report(employee_id):

    if current_user.role != "admin":

        return "Access Denied"

    employee = Employee.query.filter_by(
        employee_id=employee_id
    ).first()

    if not employee:

        return "Employee Not Found"

    prediction = Prediction.query.filter_by(
        employee_id=employee_id
    ).order_by(
        Prediction.prediction_date.desc()
    ).first()

    if not prediction:

        return "Prediction Not Found"

    import tempfile

    pdf_file = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".pdf"
    ).name

    doc = SimpleDocTemplate(
        pdf_file
    )

    styles = getSampleStyleSheet()

    content = []

    title = Paragraph(

        "Employee Attrition Report",

        styles["Title"]

    )

    content.append(title)

    content.append(
        Spacer(1,12)
    )

    content.append(
        Paragraph(
            f"<b>Employee ID:</b> {employee.employee_id}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"<b>Department:</b> {employee.department}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"<b>Job Role:</b> {employee.job_role}",
            styles["Normal"]
        )
    )

    content.append(
        Spacer(1,12)
    )

    content.append(
        Paragraph(
            f"<b>Risk Score:</b> {prediction.risk_score:.2f}%",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"<b>Status:</b> {prediction.prediction_result}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"<b>Recommendation:</b> {prediction.recommendation}",
            styles["Normal"]
        )
    )

    doc.build(
        content
    )

    return send_file(
        pdf_file,
        as_attachment=True
    )

@app.route("/admin/history")
@login_required
def prediction_history():

    if current_user.role != "admin":

        return "Access Denied"

    predictions = Prediction.query.order_by(
        Prediction.prediction_date.desc()
    ).all()

    return render_template(
        "admin/history.html",
        predictions=predictions
    )

@app.route(
    "/admin/register",
    methods=["GET","POST"]
)
def admin_register():

    form = AdminRegisterForm()

    if form.validate_on_submit():

        if form.secret_key.data != app.config["ADMIN_SECRET"]:

            flash(
                "Invalid Secret Key",
                "danger"
            )

            return redirect(
                url_for("admin_register")
            )

        # Check if email already exists
        existing_admin = User.query.filter_by(
            email=form.email.data
        ).first()

        if existing_admin:

            flash(
                "Email already registered.",
                "danger"
            )

            return redirect(
                url_for("admin_register")
            )

        hashed_password = (
            bcrypt.generate_password_hash(
                form.password.data
            ).decode("utf-8")
        )

        admin = User(

            name=form.name.data,

            email=form.email.data,

            password=hashed_password,

            role="admin"
        )

        db.session.add(admin)

        db.session.commit()

        flash(
            "Admin Registered Successfully",
            "success"
        )

        return redirect(
            url_for("admin_login")
        )

    return render_template(
        "auth/admin_register.html",
        form=form
    )

@app.route(
    "/admin/delete_employee/<employee_id>"
)
@login_required
def delete_employee(employee_id):

    if current_user.role != "admin":

        return "Access Denied"

    employee = Employee.query.filter_by(
        employee_id=employee_id
    ).first()

    if not employee:

        flash(
            "Employee Not Found",
            "danger"
        )

        return redirect(
            url_for("admin_employees")
        )

    survey = Survey.query.filter_by(
        employee_id=employee_id
    ).first()

    if survey:
        db.session.delete(survey)

    user = db.session.get(
    User,
    employee.user_id
    )

    deleted_record = DeletedEmployee(

        employee_id=employee.employee_id,

        name=user.name if user else "Unknown",

        email=user.email if user else "",

        department=employee.department,

        job_role=employee.job_role,

        deleted_by="Admin",

        exit_reason="Admin Removal"

    )

    db.session.add(
        deleted_record
    )

    db.session.delete(employee)

    if user:
        db.session.delete(user)

    db.session.commit()
    flash(
        "Employee Deleted Successfully",
        "success"
    )

    return redirect(
        url_for("admin_employees")
    )
@app.route("/delete_account", methods=["GET", "POST"])
@login_required
def delete_account():

    employee = Employee.query.filter_by(
        user_id=current_user.id
    ).first()

    if request.method == "POST":

        reason = request.form.get(
            "reason",
            "Not Specified"
        )

        if employee:

            deleted_record = DeletedEmployee(

                employee_id=employee.employee_id,

                name=current_user.name,
                email=current_user.email,

                department=employee.department,

                job_role=employee.job_role,

                deleted_by="Employee",

                exit_reason=reason

            )

            db.session.add(
                deleted_record
            )

            Survey.query.filter_by(
                employee_id=employee.employee_id
            ).delete()

            db.session.delete(
                employee
            )

        user = db.session.get(
            User,
            current_user.id
        )

        logout_user()

        db.session.delete(
            user
        )

        db.session.commit()

        flash(
            "Your account has been deleted successfully.",
            "success"
        )

        return redirect(
            url_for("home")
        )

    return render_template(
        "confirm_delete.html"
    )  

@app.route("/admin/delete_account")
@login_required
def admin_delete_account():

    if current_user.role != "admin":

        return "Access Denied"

    total_admins = User.query.filter_by(
        role="admin"
    ).count()

    deleted_count = DeletedEmployee.query.count()

    return render_template(

        "admin/dashboard.html",

        total_employees=total_employees,

        total_predictions=total_predictions,

        high_risk=high_risk,

        low_risk=low_risk,

        department_stats=department_stats,

        total_admins=total_admins,

        deleted_employees=deleted_count
    )

    if total_admins <= 1:

        flash(
            "At least one admin account must remain.",
            "danger"
        )

        return redirect(
            url_for("admin_dashboard")
        )

    user = db.session.get(
            User,
            current_user.id
    )

    logout_user()

    db.session.delete(user)

    db.session.commit()

    flash(
        "Admin account deleted successfully.",
        "success"
    )

    return redirect(
        url_for("home")
    )

@app.route("/delete_account_confirm")
@login_required
def delete_account_confirm():

    return render_template(
        "confirm_delete.html",
        delete_url=url_for(
            "delete_account"
        )
    )

@app.route("/admin/delete_account_confirm")
@login_required
def admin_delete_account_confirm():

    if current_user.role != "admin":

        return "Access Denied"

    return render_template(
        "confirm_delete.html",
        delete_url=url_for(
            "admin_delete_account"
        )
    )

@app.route("/admin/admins")
@login_required
def admin_list():

    if current_user.role != "admin":
        return "Access Denied"

    admins = User.query.filter_by(
        role="admin"
    ).all()

    return render_template(
        "admin/admins.html",
        admins=admins
    )

@app.route("/admin/deleted-employees")
@login_required
def deleted_employees():

    if current_user.role != "admin":

        return "Access Denied"

    deleted_users = DeletedEmployee.query.order_by(
        DeletedEmployee.deleted_at.desc()
    ).all()

    return render_template(

        "admin/deleted_employees.html",

        deleted_users=deleted_users
    )

if __name__ == "__main__":
    app.run()