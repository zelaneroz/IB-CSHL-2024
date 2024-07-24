#my_lib.py

#code for the database handler
import sqlite3
class database_worker:
    def __init__(self, name):
        self.connection = sqlite3.connect(name)
        self.cursor = self.connection.cursor()

    def search(self, query):
        result = self.cursor.execute(query).fetchall()
        return result

    def run_save(self, query):
        self.cursor.execute(query)
        self.connection.commit()

    def close(self):
        self.connection.close()

#code for the password hashing
from passlib.context import CryptContext

pwd_config = CryptContext(schemes=["pbkdf2_sha256"],
                            default="pbkdf2_sha256",
                            pbkdf2_sha256__default_rounds=30000
                            )
def encrypt_password(user_password):
    return pwd_config.encrypt(user_password)

def check_password(user_password,hashed):
    return pwd_config.verify(user_password, hashed)

hash = encrypt_password('bro')
print(hash)
print(check_password('bro',hash))
