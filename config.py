from cryptography.fernet import Fernet

class Config:
    SECRET_KEY = 'clinica_secret'

    SQLALCHEMY_DATABASE_URI = 'sqlite:///clinica.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    FERNET_KEY = b'6B4vVomQcUNDlm0w_EebP-tQTkEKFHPiHBiPdZyvznA='