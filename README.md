# THIS IS MY FIRST FLASK APPLICATION

## Steps:
- I created a repo at [github.com/GoodnessOlawoore/first-flask-app](https://github.com/GoodnessOlawoore/first-flask-app)
- Cloned it to my local computer via the ```git clone``` command on command prompt 
#### Input:
```
git clone command github.com/GoodnessOlawoore/first-flask-app
```
- Created a virtual environment named ```virtual-environment```(yours can be shorter) inside my **first-flask-app** folder
#### Input:
```
python -m venv virtual-environment
```
#### Why the need for a virtual environment?
Each projects require different dependencies and frameworks that they'll run on. While we may need to install different packages and frameworks for different projects, there would be conflict if this is done within a single environment housing different projects, hence, the need for a virtual environment. A virtual environment stands as an isolated environment for these projects.
- Activated the virtual environment using:
#### Input:
```
source virtual-environment/Scripts/activate
```
- After confirming that the virtual environment has been activated,
- I then installed Flask using ```pip install```
```
pip install flask
```
- Created a python file and named it ```app.py``` using the ```touch``` command
```
touch app.py
```
- Filled it with [the code](https://github.com/GoodnessOlawoore/first-flask-app/blob/main/app.py)
- Instatiated the app via the terminal by running:
```
python app.py
```
- Boom! The app is live and locally hosted!😄