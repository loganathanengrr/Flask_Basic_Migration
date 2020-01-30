import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = True
    CSRF_ENABLED = True
    SECRET_KEY = 'thisisloganathan'
    POSTGRES_URL="127.0.0.1:5432"
    POSTGRES_USER="postgres"
    POSTGRES_PW="postgres"
    POSTGRES_DB="flask_todo_db"
    SQLALCHEMY_DATABASE_URI = f'postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PW}@{POSTGRES_URL}/{POSTGRES_DB}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False