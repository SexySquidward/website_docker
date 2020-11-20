from flask_app.app import app

@app.route('/')
def index():
    return 'Hello from flask!'