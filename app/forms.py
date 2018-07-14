from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from sqlalchemy.orm import load_only
from wtforms.validators import DataRequired
from app.models import Author, Poems


def author_list():
    return Author.query


def poems_list():
    return Poems.query


class PoetryForms(FlaskForm):
    author_select = QuerySelectField(u'Select Author',
                                     query_factory=author_list, allow_blank=False, get_label='author')
    poem_select = QuerySelectField(u'Select Poems',
                                   query_factory=poems_list, allow_blank=False, get_label='title')
    submit = SubmitField('Submit')
