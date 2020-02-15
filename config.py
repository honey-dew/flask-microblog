from secrets import token_hex

class Config(object):

	SECRET_KEY = token_hex(24)