# Installation Guide

Open a terminal and type.

```
python -m venv .venv
```

This creates a .venv folder inside the project. That folder contains a separate Python environment for this project.

Next, you activate it.
## Activate virtual environment

On Windows PowerShell:
```
.venv\Scripts\Activate.ps1
```
If the prompt changes to include (.venv), that is evidence that the environment is active.

NB: You might get an error here regarding running PowerShell scripts.  To resolve that run:
```
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```
Then you upgrade pip:
```
python -m pip install --upgrade pip
```
This matters because pip is the tool that installs Python packages. Using python -m pip is clearer than just typing pip, because it makes sure the package installer belongs to the currently selected Python interpreter.

Example package install

If the project later needs a package such as requests, you would install it like this:
```
pip install flask
```

Your first flask app

Add an app.py file with the following code:

```
# app.py
from flask import Flask
app = Flask(__name__)
@app.route("/")
def greet():
    return "Hello, World!"
```

How to run it

```

flask run
```
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

Check stuff before i do other stuff.

Attempting to do stuff
