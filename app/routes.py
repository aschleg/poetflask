from flask import render_template, flash, redirect, request

from app import app
from app.forms import PoetryForms
from app.models import Author, Poems, db
from sqlalchemy.orm import load_only


db.create_all()


@app.route('/', methods=['get', 'post'])
@app.route('/index', methods=['get', 'post'])
def index():
    form = PoetryForms()

    #if request.method == 'POST':
    author = request.form.get('selectauthor')

    author_poems = Poems.query.filter_by(author=author).all()

    #if poet_form.validate_on_submit():
    #    author = Author.query.filter_by(author=poet_form.author_select.data).first()

    return render_template('index.html', title='Poetflask', form=form, author_poems=author_poems)
