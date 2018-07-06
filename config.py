import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ['POETFLASK_SECRET_KEY']
    SQLALCHEMY_DATABASE_URI = os.environ['POETFLASK_DATABASE_URI']
    SQLALCHEMY_TRACK_MODIFICATIONS = False
