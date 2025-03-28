# Configuração da aplicação
# Obs: Ainda não configurado com as nossas informações, somente o template
import os

class Config(object):
	"""
	Configuration base, for all environments.
	"""
	DEBUG = False
	TESTING = False
	SQLALCHEMY_DATABASE_URI = 'postgresql://teste_server_v1_user:ifLn9EkDWAbNo5d7KtbrDAiGnQ2NBTNE@dpg-cv5nkc3tq21c73da9hi0-a.oregon-postgres.render.com/teste_server_v1'
	SQLALCHEMY_TRACK_MODIFICATIONS = False

	#Get your reCaptche key on: https://www.google.com/recaptcha/admin/create
	#RECAPTCHA_PUBLIC_KEY = "6LffFNwSAAAAAFcWVy__EnOCsNZcG2fVHFjTBvRP"
	#RECAPTCHA_PRIVATE_KEY = "6LffFNwSAAAAAO7UURCGI7qQ811SOSZlgU69rvv7"

class ProductionConfig(Config):
	SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL','postgresql://teste_server_v1_user:ifLn9EkDWAbNo5d7KtbrDAiGnQ2NBTNE@dpg-cv5nkc3tq21c73da9hi0-a.oregon-postgres.render.com/teste_server_v1')
	SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
	DEBUG = True

class TestingConfig(Config):
	TESTING = True