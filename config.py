import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')
    ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL')
    LANGUAGES = ['en', 'hi']
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = 1
    MAIL_USERNAME = 'celestial25.dev@gmail.com'
    MAIL_PASSWORD = '' #hidden
    ADMINS = ['celestial25.dev@gmail.com']
    POSTS_PER_PAGE = 25
