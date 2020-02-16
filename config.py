from secrets import token_hex
import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):

	SECRET_KEY = token_hex(24)

	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')or \
	'sqlite:///' + os.path.join(basedir, 'app.db')

	SQLALCHEMY_TRACK_MODIFICATIONS = False