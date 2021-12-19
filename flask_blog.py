from flask import Flask, render_template, url_for
app = Flask(__name__)


posts = [
    {
        'author': 'Simon',
        'title': 'Blog post one',
        'content': 'First post content',
        'dateposted': 'April 21 2021',
    },
    {
        'author': 'John Doe',
        'title': 'Blog post two',
        'content': 'Second post content',
        'dateposted': 'April 22 2021',
    },
]


@app.route('/')
@app.route('/home')
def hello():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)
