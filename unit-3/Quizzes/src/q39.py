from kivymd.app import MDApp

class q39(MDApp):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.count = 0

    def build(self):
        return
    def add_count(self):
        self.count +=1
        self.root.ids.counter.text = f"Counter {self.count}"


test = q39()
test.run()

