from kivymd.app import MDApp
class task1(MDApp):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.converted=0
        self.amount=0
        self.type="eur"
    def build(self):
        return
    def set_input(self):
        input = self.root.ids.user_input.text
        if input.isnumeric()==False:
            self.root.ids.output.text = "Please enter an integer"
        else:
            self.amount = int(input)
    def to_jpy(self):
        converted=0
        converted = round(self.amount*141.21)
        self.root.ids.output.text = f"¥ {converted}"

    def to_usd(self):
        converted=0
        converted = round(self.amount*1.08)
        self.root.ids.output.text = f"$ {converted}"

test=task1()
test.run()