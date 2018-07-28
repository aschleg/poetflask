from flask import render_template, flash, redirect, request
from sqlalchemy import func

from app import app
from app.models import Author, Poems, db


db.create_all()


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():

    return render_template('index.html', title='Poetflask')


@app.route('/authors/', methods=['GET', 'POST'])
def authors_list():
    author_list = Author.query.all()

    # author_poem_count = Poems.query.\
    #     with_entities(Poems.author, func.count(Poems.title).label('poem_count')).\
    #     group_by(Poems.author).\
    #     order_by(Poems.author.asc())\
    #     .all()
    title = 'Poets'
    return render_template('authors.html', author_list=author_list, title=title)


@app.route('/authors/<author>/', methods=['GET', 'POST'])
def author_page(author):
    author_poems = Poems.query.filter_by(author=author).all()
    author_info = Author.query.filter_by(author=author).first()

    return render_template('author.html', author_poems=author_poems, author_info=author_info,
                           author_name=author)


@app.route('/about', methods=['GET', 'POST'])
def about():

    return render_template('about.html')
