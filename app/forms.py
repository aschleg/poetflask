from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from sqlalchemy.orm import load_only
from wtforms.validators import DataRequired
from app.models import Poet, Poems


def poet_list():
    return Poet.query


def poems_list():
    return Poems.query


class PoetryForms(FlaskForm):
    poet_select = QuerySelectField(u'Select Poet',
                                   query_factory=poet_list, allow_blank=False, get_label='name')

    poem_select = QuerySelectField(u'Select Poems',
                                   query_factory=poems_list, allow_blank=False, get_label='title')

    submit = SubmitField('Submit')
