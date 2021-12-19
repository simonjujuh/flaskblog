from flask import Flask
app = Flask(__name__)


@app.route('/')
@app.route('/home')
def hello():
    return "<h1>Home page</h1>"

@app.route('/about')
def about():
    return "Flask blog version 0.1-alpha release"

if __name__ == '__main__':
    app.run(debug=True)
