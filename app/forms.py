from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired
from app.models import Author, Poems


def author_list():
    # return Author.query.filter_by(enabled=True).all()
    return Author.query.all()


def poems_list():
    return Poems.query.all()


class PoetryForms(FlaskForm):
    author_search = QuerySelectField(u'Select Author',
                                     query_factory=author_list, allow_blank=True)

    poem_search = QuerySelectField(u'Select Poems',
                                   query_factory=poems_list, allow_blank=True)
