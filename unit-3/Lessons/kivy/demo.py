from kivymd.app import MDApp

class layout_demo(MDApp):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.count = 0

    def build(self):
        return

    def set_counter(self):
        #validate that it is a digit
        user_start = int(self.root.ids.user_start_x.text)
        self.root.ids.counter_label.text = f"x={self.count}"

    def change(self, name:str):
        if 'up' in name:
            self.count += 1
        else:
            self.count -= 1
        self.root.ids.counter_label.text = f"x={self.count}"

demo_class = layout_demo()
demo_class.run()
