from project import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, world."
