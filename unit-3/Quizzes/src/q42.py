from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen

class MysteryPageA(MDScreen):
    def message1(self):
        self.ids.texta.text = "This is mystery page A you pressed the button"

class MysteryPageB(MDScreen):
    def message2(self):
        self.ids.textb.text = "This is mystery page B you pressed the button"

class Mystery(MDApp):
    def build(self):
        return

test = Mystery()
test.run()