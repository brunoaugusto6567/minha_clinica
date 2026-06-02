class Config:
    SECRET_KEY = 'clinica_secret'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///clinica.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False