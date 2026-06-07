from cryptography.fernet import Fernet
from config import Config

fernet = Fernet(Config.FERNET_KEY)

def criptografar(texto):
    return fernet.encrypt(texto.encode()).decode()

def descriptografar(texto):
    return fernet.decrypt(texto.encode()).decode()