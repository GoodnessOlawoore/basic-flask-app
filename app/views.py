from app import app

@app.route("/")
def index():
    return "This is the home page"

@app.route("/about")
def about():
    return "This is the about me page"