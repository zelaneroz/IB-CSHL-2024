from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen

class LoginScreen(MDScreen):
    def try_login(self):
        print("User tried to login")
        print(f"Username: {self.ids.uname.text}\nPassword: {self.ids.passwd.text}")
class RegistrationScreen(MDScreen):
    def try_register(self):
        print("User tried to register")
class samplelogin(MDApp):
    def build(self):
        return

test = samplelogin()
test.run()
