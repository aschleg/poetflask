from flask import jsonify, render_template, request

from app import app
from app.models import Poet, Poems, PoetOfTheDay, db
from apscheduler.schedulers.background import BackgroundScheduler
import datetime

from random import randint

db.create_all()


def update_poet_of_the_day_table_job():
    today = datetime.datetime.today().strftime('%Y-%m-%d')

    previous_poets = PoetOfTheDay.query(PoetOfTheDay.author)
    previous_poets = [i[0] for i in previous_poets]

    poet_list = Poet.query(Poet.name)
    poet_list = [i[0] for i in poet_list]

    available_poets = list(set(poet_list) - set(previous_poets))

    poet_of_the_day = available_poets[randint(0, len(available_poets))]

    poet_of_the_day_update = PoetOfTheDay(author=poet_of_the_day,
                                          date=today)

    db.session.add(poet_of_the_day_update)

    db.session.commit()

    return jsonify(result={'poet': poet_of_the_day,
                           'date': today})


scheduler = BackgroundScheduler()
poet_of_the_day_job = scheduler.add_job(update_poet_of_the_day_table_job, 'interval', minutes=60 * 24)
scheduler.start()
scheduler.print_jobs()


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
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


@app.route('/about/')
def about():
    return render_template('about.html')


@app.route('/selected_poetry', methods=['POST'])
def selected_poetry():
    poet = request.json['poet']

    return jsonify({'poet': poet})


@app.template_filter()
def poem_sample(poem):
    sample = str(poem).splitlines()[0:2]

    sample_poem = ''
    for line in sample:
        sample_poem = sample_poem + line.strip() + ' <br /> '

    return sample_poem
