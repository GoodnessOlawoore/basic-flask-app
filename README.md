# CREATE A BASIC FLASK APPLICATION
You can follow the steps below to run your first app, but do note that the repository has been restructured to contain more code, therefore codes_in_repo != README.md
## Steps:
- I created a repo at [github.com/GoodnessOlawoore/basic-flask-app](https://github.com/GoodnessOlawoore/basic-flask-app)
- Cloned it to my local computer via the command prompt using:

```
git clone command github.com/GoodnessOlawoore/first-flask-app
```
- Created a virtual environment named ```venv``` (yours can be "env") inside my **first-flask-app** folder using:

```
python -m venv venv
```
#### Why the need for a virtual environment?
Each projects require different dependencies and frameworks that they'll run on. While we may need to install different packages and frameworks for different projects, there would be conflict if this is done within a single environment housing different projects, hence, the need for a virtual environment. A virtual environment stands as an isolated environment for these/each projects.
- Activated the virtual environment using:

```
source venv/Scripts/activate
```
- After confirming that the virtual environment has been activated,
- I then installed Flask using:

```
pip install flask
```
- Created a python file and named it ```app.py``` using:
```
touch app.py
```
- Filled it with [the code](https://github.com/GoodnessOlawoore/basic-flask-app/blob/main/app.py) (yours will be different)
- Instatiated the app via the terminal using:
```
python app.py 
```
- You can also use ```flask run```
- Boom! The app is live and running locally on  ```http://127.0.0.1:5000```😄
