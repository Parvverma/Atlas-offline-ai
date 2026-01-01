import os
import subprocess

SAFE_APPS = {
    "notepad": "notepad.exe",
    "calculator": "calc.exe"
}

def open_app(app_name):
    app = SAFE_APPS.get(app_name.lower())
    if not app:
        return "❌ App not allowed."
    subprocess.Popen(app)
    return f"Opened {app_name}"
