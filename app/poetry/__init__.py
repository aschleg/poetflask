from flask import Blueprint

poetry_bp = Blueprint('poetry_bp', __name__,
                      template_folder='templates')

from app.poetry import views
