import os

SECRET_KEY = os.urandom(32)

base_dir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

SQLALCHEMY_DATABASE_URI = 'sqlite:////' + os.path.join(base_dir, 'data.db')

SQLALCHEMY_TRACK_MODIFICATIONS = False