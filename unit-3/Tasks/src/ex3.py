from kivymd.app import MDApp

class ex3(MDApp):
    def build(self):
        return

    def change_author(self,name):
        self.root.ids.text.text = f"Author {name}"

test = ex3()
test.run()