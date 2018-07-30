from flask import render_template, flash, redirect, request
from sqlalchemy import func

from app import app
from app.models import Poet, Poems, db

from random import randint

db.create_all()


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():

    poem_count = Poems.query.count()

    random_id = randint(1, poem_count)

    random_poem = Poems.query.filter_by(id=random_id).first()

    return render_template('index.html', title='Welcome to Poetflask!', random_poem=random_poem)


@app.route('/poets/', methods=['GET', 'POST'])
def poets_list():
    poet_list = Poet.query.order_by(Poet.last_name.asc()).all()

    # author_poem_count = Poems.query.\
    #     with_entities(Poems.author, func.count(Poems.title).label('poem_count')).\
    #     group_by(Poems.author).\
    #     order_by(Poems.author.asc())\
    #     .all()
    title = 'Poets'
    return render_template('poets.html', poet_list=poet_list, title=title)


@app.route('/poets/<poet>/', methods=['GET', 'POST'])
def poet_page(poet):
    author_poems = Poems.query.filter_by(author=poet).all()
    poet_info = Poet.query.filter_by(name=poet).first()

    return render_template('poet.html', author_poems=author_poems, poet_info=poet_info,
                           author_name=poet)


@app.route('/about', methods=['GET', 'POST'])
def about():

    return render_template('about.html')
