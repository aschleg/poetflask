from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class PoetryForms(FlaskForm):
    search_type = StringField('Search Type', validators=[DataRequired()])
