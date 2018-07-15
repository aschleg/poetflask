from flask import render_template, flash, redirect, request

from app import app
from app.forms import PoetryForms
from app.models import Author, Poems, db


db.create_all()


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = PoetryForms()
    author = None

    if request.method == 'POST':
        author = form.author_select.data.author

    author_poems = Poems.query.filter_by(author=author).all()

    return render_template('index.html', title='Poetflask', form=form, author_poems=author_poems)


@app.route('/authors', methods=['GET', 'POST'])
def authors_list():
    author_list = Author.query.all()

    return render_template('authors.html', author_list=author_list)


@app.route('/authors/<author>/', methods=['GET', 'POST'])
def author_poetry(author):
    form = PoetryForms()

    if request.method == 'POST':
        author = form.author_select.data.author

    author_poems = Poems.query.filter_by(author=author).all()

    return render_template('author.html', author_poems=author_poems, author_name=author)#, author=author)
