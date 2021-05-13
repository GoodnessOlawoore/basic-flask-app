from app import app

@app.route("/staff/dashboard")
def staff_dashboard():
    return "Staff dashboard comes here!"

@app.route("/staff/profile")
def staff_profile():
    return "Staff profile comes here!"