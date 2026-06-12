# 🚀 Employee Attrition Prediction System

> 🎯 An AI-Powered HR Analytics Platform for Predicting Employee Attrition and Improving Workforce Retention

---

## 📌 Overview

The **Employee Attrition Prediction System** is a Machine Learning and Full-Stack Web Application designed to help organizations identify employees who may be at risk of leaving the company.

By analyzing employee information, workplace satisfaction surveys, and behavioral indicators, the system predicts attrition risk and provides actionable HR recommendations to improve employee retention and organizational stability.

---

## ✨ Key Features

### 🔐 Authentication & Security

* 👤 Employee Registration & Login
* 👨‍💼 Admin Registration & Login
* 🔒 Secure Password Hashing using Bcrypt
* 🛡️ Role-Based Access Control
* 🚪 Logout Functionality
* ❌ Self Account Deletion

---

### 👨‍💼 Employee Management

* 📝 Employee Profile Creation
* 🔍 Employee Search
* 📋 Employee Record Management
* 🗑️ Employee Deletion by Admin
* 📊 Employee Dashboard

---

### 📑 Employee Survey System

The system collects employee satisfaction data through intelligent surveys covering:

* 😊 Job Satisfaction
* 🏢 Work Environment Satisfaction
* ⚖️ Work-Life Balance
* 🤝 Relationship Satisfaction
* 👨‍💼 Manager Support
* 📈 Career Growth Opportunities
* 💰 Salary Satisfaction
* 🏆 Recognition & Rewards
* 😓 Stress Level
* 🔐 Job Security

---

### 🤖 AI & Machine Learning Engine

* ⚡ XGBoost-Based Prediction Model
* 🎯 Employee Attrition Risk Prediction
* ❤️ Employee Wellness Score Calculation
* 📊 Risk Adjustment Using Survey Insights
* 🧠 Explainable AI Support
* 💡 Personalized Retention Recommendations

---

### 📈 HR Analytics Dashboard

* 👥 Total Employee Overview
* 🟢 Active Employee Tracking
* 🏢 Department Distribution Analysis
* ⚠️ Attrition Risk Monitoring
* 📚 Prediction History Tracking
* 📊 Department-Level Insights

---

### 📄 Reporting System

* 📑 Detailed Prediction Reports
* 🖨️ PDF Report Generation
* 📋 Historical Prediction Records
* 📈 Risk Assessment Summaries

---

### 🎨 Modern User Experience

* 🌙 Dark Mode Support
* ☀️ Light Mode Support
* 📱 Fully Responsive Design
* ⚡ Interactive Dashboards
* 🎯 Bootstrap 5 UI
* ✨ Modern Glassmorphism Components

---

## 🏗️ System Workflow

```text
Employee Data
      +
Survey Responses
      +
Machine Learning Model
      +
Risk Adjustment Engine
      +
Recommendation System
      ↓
Attrition Prediction
      +
HR Insights
      +
Retention Recommendations
```

---

## 🛠️ Technology Stack

### Backend ⚙️

* Python
* Flask
* SQLAlchemy
* Flask-Login
* Flask-WTF
* Bcrypt

### Database 🗄️

* SQLite

### Machine Learning 🧠

* XGBoost
* Scikit-Learn
* Pandas
* NumPy
* SHAP Explainability

### Frontend 🎨

* HTML5
* CSS3
* Bootstrap 5
* JavaScript
* Jinja2

### Reporting 📄

* PDF Report Generation

---

## 📂 Project Structure

```text
EMPLOYEE PROJECT

├── app.py
├── config.py
├── forms.py
├── models.py
├── requirements.txt

├── machine_learning
│   ├── train_model.py
│   ├── predict.py
│   ├── preprocess.py
│   ├── recommendation.py
│   ├── shap_analysis.py
│   ├── model.pkl
│   ├── scaler.pkl
│   └── encoders.pkl

├── routes
│   ├── auth_routes.py
│   ├── admin_routes.py
│   ├── employee_routes.py
│   └── prediction_routes.py

├── templates
│   ├── admin
│   ├── employee
│   └── auth

├── static

└── database
```

---

## ⚙️ Installation

### 1️⃣ Clone Repository

```bash
[git clone ](https://github.com/niranjanhegde-droid/AI_Employee_Attrition_Prediction_System.git)```

### 2️⃣ Move Into Project

```bash
cd employee-attrition-prediction-system
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run Application

```bash
python app.py
```

### 5️⃣ Open Browser

```text
http://127.0.0.1:5000
```

---

## 🎯 How It Works

### Employee Side

1. 👤 Register Account
2. 📝 Complete Profile
3. 📑 Submit Survey
4. 📊 View Dashboard

### Admin Side

1. 👨‍💼 Login
2. 👥 Manage Employees
3. 🤖 Predict Attrition Risk
4. 📈 Analyze Results
5. 📄 Download Reports

---

## 📊 Prediction Output

The system provides:

* 🎯 Attrition Risk Score
* 🟢 Low Risk Classification
* 🟡 Medium Risk Classification
* 🔴 High Risk Classification
* ❤️ Wellness Score
* 💡 Retention Recommendations
* 📄 Detailed PDF Reports

---

## 🚀 Future Enhancements

* 🧠 Attrition Persona Classification
* 📊 Attrition Driver Ranking
* 🎯 Retention Impact Simulator
* 📧 Email Notification System
* 🤖 AI HR Assistant
* 📈 Workforce Trend Forecasting
* ☁️ Cloud Deployment
* 📡 Real-Time Analytics

---

## 🎓 Learning Outcomes

This project demonstrates:

* 🤖 Machine Learning Applications
* 📊 HR Analytics
* 🧠 Explainable AI
* 🌐 Full Stack Development
* 🔐 Authentication & Security
* 🗄️ Database Management
* 📈 Data Visualization
* 📄 Automated Reporting

---

## 👨‍💻 Author

### Niranjan Hegde

🎓 Postgraduate Student
💻 Full Stack Developer
🤖 AI & Machine Learning Enthusiast

---

## ⭐ Support

If you found this project useful:

⭐ Star the repository

🍴 Fork the repository

📢 Share with others

---

## 📜 License

This project is developed for educational and academic purposes.
