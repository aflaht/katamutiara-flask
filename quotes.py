from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# localhost
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://zak:123456@localhost/quotes'
# heroku
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://ayzhwykmhihhlu:39769e4abae1c9e9e79e2b9e2f004ce984cc926de7e1a13b42948571e00edfd6@ec2-54-195-246-55.eu-west-1.compute.amazonaws.com:5432/dde31v7gvb6edg'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

'''
> from quotes import db
> db.create_all()
'''


class Favquotes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(30))
    quote = db.Column(db.String(2000))


@app.route('/')
def index():
    result = Favquotes.query.all()
    return render_template('index.html', result=result)


@app.route('/about')
def about():
    cities = ['Jakarta', 'Semarang', 'Surabaya', 'Mataram']
    return render_template('about.html', quote='Kindness needs no translation', cities=cities)


@app.route('/quotes')
def quotes():
    return render_template('quotes.html')


@app.route('/process', methods=['POST'])
def process():
    author = request.form['author']
    quote = request.form['quote']
    quotedata = Favquotes(author=author, quote=quote)
    db.session.add(quotedata)
    db.session.commit()
    return redirect(url_for('index'))
