from flask import jsonify, render_template, request

from app import app
from app.models import Poet, Poems, db

from random import randint

db.create_all()


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():

    poem_count = Poems.query.count()

    random_id = randint(1, poem_count)

    #poet_of_the_day

    random_poem = Poems.query.filter_by(id=random_id).first()

    return render_template('index.html', title='Welcome to Poetflask!', random_poem=random_poem)


@app.route('/poets/', methods=['GET', 'POST'])
def poets_list():
    poet_list = Poet.query.order_by(Poet.last_name.asc()).all()

    title = 'Poets'
    return render_template('poets.html', poet_list=poet_list, title=title)


@app.route('/poets/<poet>/', methods=['GET', 'POST'])
def poet_page(poet):
    author_poems = Poems.query.filter_by(author=poet).all()
    poet_info = Poet.query.filter_by(name=poet).first()

    return render_template('poet.html', author_poems=author_poems, poet_info=poet_info,
                           author_name=poet)


@app.route('/poetry/', methods=['GET', 'POST'])
def poetry_page():
    poet_list = Poet.query.order_by(Poet.last_name.asc()).all()

    return render_template('poetry.html', poet_list=poet_list)


@app.route('/selected_poetry', methods=['POST'])
def selected_poetry():
    poet = request.json['poet']

    return jsonify({'poet': poet})


@app.route('/about/')
def about():
    return render_template('about.html')


@app.template_filter()
def poem_sample(poem):
    return '\n'.join(str(poem).splitlines()[0:2])
