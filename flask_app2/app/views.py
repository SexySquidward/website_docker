from app import app

@app.route('/app')
def index():
    return 'Hello from flask!'
