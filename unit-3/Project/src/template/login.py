import sqlite3
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen

class database_handler:
    def __init__(self, namedb:str):
        self.connection = sqlite3.Connection(namedb)
        self.cursor = self.connection.cursor()

    def create_tables(self):
        query = f"""CREATE TABLE if not exists users(
    id integer primary key,
    email text not null unique,
    password text not null,
    username text not null
)"""

    def run_query(self,query:str):
        self.cursor.execute(query)
        self.connection.commit()

    def close(self):
        self.connection.close()

    def insert(self,email,password,username):
        query = f"INSERT into users VALUES('{email}','{password}','{username}')"
        self.run_query(query)

    def test_login(self, email, passwd):
        self.cursor.execute("SELECT * FROM users")
        email_list,uname_list = [],[]
        print(email)
        for i in self.cursor.fetchall():
            email_list.append(i[1])
            uname_list.append(i[3])
        print(email_list)
        print(uname_list)
        output=""
        if (email in email_list or email in uname_list) and email != "":
            self.cursor.execute(f"SELECT password FROM users where email='{email}' or username='{email}'")
            for j in self.cursor:
                if passwd == j[0]:
                    output="You have successfully logged in!"
                else:
                    output="Incorrect Password"
        else:
            output="Incorrect Email"
        print(output)
        if output=="You have successfully logged in!":
            return True


class LoginScreen(MDScreen):
    def try_login(self):
        email_entered = self.ids.uname.text
        pass_entered = self.ids.passwd.text
        db = database_handler(namedb="login_database.db")
        if db.test_login(email=email_entered,passwd=pass_entered)==True:
            self.parent.current = "MainScreen"

    def try_register(self):
        print("User tried to register")
        self.parent.current = "RegistrationScreen"
        #print("User tried to login")
        #print(f"Username: {self.ids.uname.text}\nPassword: {self.ids.passwd.text}")
class RegistrationScreen(MDScreen):
    def try_register(self):
        print("User tried to register")
        self.parent.current = "RegistrationScreen"
class MainScreen(MDScreen):
    pass
class login(MDApp):
    def build(self):
        return
db = database_handler(namedb="login_database.db")
db.create_tables()
db.close()
test = login()
test.run()
