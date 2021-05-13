from app import app

@app.route("/student/dashboard")
def student_dashboard():
    return "Student dashboard comes here!"

@app.route("/student/profile")
def student_profile():
    return "Student profile comes here!"