# CREATE A BASIC FLASK APPLICATION
You can follow the steps below to run your first app, but do note that the repository has been restructured to contain more code, therefore codes_in_repo != README.md
## Steps:
- Create a repo like this: [github.com/GoodnessOlawoore/basic-flask-app](https://github.com/GoodnessOlawoore/basic-flask-app)
- Clone it to your local computer via the command prompt using the "git clone" command:

```
git clone github.com/GoodnessOlawoore/basic-flask-app
```
-(use the path/link to the new repo you created)

- Create a virtual environment using ```python -m venv env``` ,where "env" is your virtual environment

#### Why the need for a virtual environment?
Each projects require different dependencies and frameworks that they'll run on. While we may need to install different packages and frameworks for different projects, there would be conflict if this is done within a single environment housing different projects, hence, the need for a virtual environment. A virtual environment stands as an isolated environment for these/each projects.
- Activate the virtual environment using:

```
source env/Scripts/activate
```
- After confirming that the virtual environment is activated,
- Install Flask using:

```
pip install flask
```
- Create a python file and name it ```app.py``` using:
```
touch app.py
```
- Fill it with the lines of code below:
```
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
      return "This is a basic app"

if __name__ == "__main__:
      app.run()
```
- Instatiate the app via the terminal using: ``` python app.py ``` or ```flask run```
- Boom! The app is live and running locally on  ```http://127.0.0.1:5000```😄
