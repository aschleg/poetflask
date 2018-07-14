from flask import render_template, flash, redirect, request

from app import app
from app.forms import PoetryForms
from app.models import Author, Poems, db


db.create_all()


@app.route('/', methods=['GET', 'POST'])
def index():
    form = PoetryForms()
    author = None

    if request.method == 'POST':
        author = form.author_select.data.author

    author_poems = Poems.query.filter_by(author=author).all()

    return render_template('index.html', title='Poetflask', form=form, author_poems=author_poems)


# @app.route('/author', methods=['GET', 'POST'])
# def author():
#     author = request.form['author_select']
#     author_poems = Poems.query.filter_by(author=author).all()
#
#     return render_template('author.html', author_poems=author_poems, author=author)
