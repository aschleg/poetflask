import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ['POETFLASK_DATABASE_URI']
    SQLALCHEMY_TRACK_MODIFICATIONS = False
