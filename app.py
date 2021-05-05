from flask import Flask
#Disregard any error text on the import code block, that is a linter issue

app = Flask(__name__)

@app.route("/")
def index():
    return "This is my first Flask app!"

if __name__ == "__main__":
    app.run() 