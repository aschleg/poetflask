import datetime
from flask import jsonify, render_template, request
from sqlalchemy import and_

from app import db
from app.models import PoetOfTheDay, Poet, Poems

from random import randint
from app.poetry import poetry_bp


# def update_poet_of_the_day_table_job():
#     today = datetime.datetime.today().strftime('%Y-%m-%d')
#
#     previous_poets = PoetOfTheDay.query(PoetOfTheDay.author)
#     previous_poets = [i[0] for i in previous_poets]
#
#     poet_list = Poet.query(Poet.name)
#     poet_list = [i[0] for i in poet_list]
#
#     available_poets = list(set(poet_list) - set(previous_poets))
#
#     poet_of_the_day = available_poets[randint(0, len(available_poets))]
#
#     poet_of_the_day_update = PoetOfTheDay(author=poet_of_the_day,
#                                           date=today)
#
#     db.session.add(poet_of_the_day_update)
#
#     db.session.commit()
#
#     return jsonify(result={'poet': poet_of_the_day,
#                            'date': today})


@poetry_bp.route('/poets/', methods=['GET', 'POST'])
def poets():
    poet_list = Poet.query.order_by(Poet.last_name.asc()).all()

    title = 'Poets'
    return render_template('poets.html', poet_list=poet_list, title=title)


@poetry_bp.route('/poets/<poet>/', methods=['GET', 'POST'])
def poet(poet):
    author_poems = Poems.query.filter_by(author=poet).all()
    poet_info = Poet.query.filter_by(name=poet).first()

    return render_template('poet.html', author_poems=author_poems, poet_info=poet_info,
                           author_name=poet)


@poetry_bp.route('/poetry/', methods=['GET', 'POST'])
def poetry():
    poet_list = Poet.query.order_by(Poet.last_name.asc()).all()
    poem_list = db.session.query(Poems.title).all()

    min_poet_birth = db.session.query(Poet.year_of_birth).\
        order_by(Poet.year_of_birth).\
        first()[0]

    max_poet_birth = db.session.query(Poet.year_of_birth).\
        order_by(Poet.year_of_birth.desc()).\
        filter(Poet.year_of_birth != None).\
        first()[0]

    return render_template('poetry.html', poet_list=poet_list, poem_list=poem_list,
                           min_poet_birth=min_poet_birth, max_poet_birth=max_poet_birth)


@poetry_bp.route('/poetry_search', methods=['GET'])
def poetry_search():
    poet = request.args.get('poet')
    poet_gender = request.args.get('poet_gender')
    poet_born_before = request.args.get('poet_born_before')
    poet_born_after = request.args.get('poet_born_after')
    poem = request.args.get('poem')

    if poem not in (None, ''):
        search_result = db.session.query(Poems.title, Poems.lines).\
            filter(Poems.title == poem)

    else:
        search_result = db.session.query(Poems.title, Poet.name, Poet.gender, Poet.year_of_birth, Poems.lines).\
            outerjoin(Poet, Poems.author == Poet.name).\
            filter(
                and_(Poet.year_of_birth <= poet_born_before,
                     Poet.year_of_birth >= poet_born_after))

        if poet not in (None, ''):
            search_result = search_result.filter_by(name=poet)

        if poet_gender not in (None, ''):
            search_result = search_result.filter_by(gender=poet_gender)

    results = search_result

    result_dict = {}

    r = 0
    for result in results:
        result_dict['result' + str(r)] = [result[1], result[4]]
        r += 1

    print(result_dict)

    return jsonify(result_dict)


@poetry_bp.app_template_filter()
def poem_sample(poem):
    sample = str(poem).splitlines()[0:2]

    sample_poem = ''
    for line in sample:
        sample_poem = sample_poem + line.strip() + ' <br /> '

    return sample_poem
