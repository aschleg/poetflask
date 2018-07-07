from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired


class PoetryForms(FlaskForm):
    author_search = SelectField('Search Author')
    poem_search = SelectField('Select Poem')