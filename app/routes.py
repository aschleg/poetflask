from flask import render_template, flash, redirect

from app import app
from app.forms import PoetryForms
from app.models import Author, Poems, db


db.create_all()


@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    poet_form = PoetryForms()
    if poet_form.validate_on_submit():
        flash('Author {}, Poem {}'.format(poet_form.author_search, poet_form.poem_search))
    return render_template('index.html', title='Poetflask', form=poet_form)


#@app.route('/author_search', methods=['GET'])
#def author_search():
#    form = PoetryForms()
#    if form.validate_on_submit():
#        pass
