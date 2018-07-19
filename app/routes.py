from flask import render_template, flash, redirect, request
from sqlalchemy import func

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

    author_poems = Poems.query.\
        filter_by(author=author).\
        all()

    return render_template('index.html', title='Poetflask', form=form, author_poems=author_poems)


@app.route('/authors', methods=['GET', 'POST'])
def authors_list():
    author_list = Author.query.all()
    author_poem_count = Poems.query.\
        with_entities(Poems.author, func.count(Poems.title).label('poem_count')).\
        group_by(Poems.author).\
        order_by(Poems.author.asc())\
        .all()

    return render_template('authors.html', author_list=author_list, author_poem_count=author_poem_count)


@app.route('/authors/<author>/', methods=['GET', 'POST'])
def author_poetry(author):
    author_poems = Poems.query.filter_by(author=author).all()

    return render_template('author.html', author_poems=author_poems)


@app.route('/about', methods=['GET', 'POST'])
def about():

    return render_template('about.html')
