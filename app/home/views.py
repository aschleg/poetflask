import datetime
from flask import render_template

from app import db
from app.models import Poems, PoetOfTheDay, Poet

from random import randint
from app.home import home_bp


@home_bp.route('/', methods=['GET', 'POST'])
@home_bp.route('/index', methods=['GET', 'POST'])
def index():

    poem_count = Poems.query.count()

    random_id = randint(1, poem_count)

    poet_of_the_day = db.session.query(PoetOfTheDay.author).\
        filter_by(date=datetime.datetime.today().strftime('%Y-%m-%d')).\
        first()[0]

    poet_of_the_day = Poet.query.filter_by(name=poet_of_the_day).first()

    random_poem = Poems.query.filter_by(id=random_id).first()

    return render_template('index.html', title='Welcome to Poetflask!',
                           random_poem=random_poem, poet_of_the_day=poet_of_the_day)


@home_bp.route('/about/')
def about():
    return render_template('about.html')
