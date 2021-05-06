# THIS IS MY FIRST FLASK APPLICATION

## Steps:
- I created a repo at [github.com/GoodnessOlawoore/first-flask-app](https://github.com/GoodnessOlawoore/first-flask-app)
- Cloned it to my local computer via the command prompt using:

```
git clone command github.com/GoodnessOlawoore/first-flask-app
```
- Created a virtual environment named ```virtual-environment```(yours can be shorter) inside my **first-flask-app** folder using:

```
python -m venv virtual-environment
```
#### Why the need for a virtual environment?
Each projects require different dependencies and frameworks that they'll run on. While we may need to install different packages and frameworks for different projects, there would be conflict if this is done within a single environment housing different projects, hence, the need for a virtual environment. A virtual environment stands as an isolated environment for these/each projects.
- Activated the virtual environment using:

```
source virtual-environment/Scripts/activate
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
- Filled it with [the code](https://github.com/GoodnessOlawoore/first-flask-app/blob/main/app.py)
- Instatiated the app via the terminal using:
```
python app.py
```
- Boom! The app is live and running locally on  ```http://127.0.0.1:5000```😄