from doctest import debug
from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [
    {
        'Author': 'Mayank Singh Rawat',
        'Title': 'Learn Python Flask',
        'Date_posted': 'October 2019',
        'Content': 'Dummy content 1'
    },
    {
        'Author': 'Mitali Rawat',
        'Title': 'How to crack coding Interview',
        'Date_posted': 'September 2019',
        'Content': 'Dummy content 2'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)
