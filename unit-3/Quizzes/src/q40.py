from kivymd.app import MDApp
import warnings
warnings.simplefilter('ignore')

class q40(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.colors = ["black","white","red","blue"]
    def build(self):
        return
    def color(self):
        if self.root.ids.main1.md_bg_color == self.colors[1]:
            self.root.ids.main1.md_bg_color = self.colors[0]
            self.root.ids.btn1.md_bg_color = self.colors[2]
            self.root.ids.txt.text_color = self.colors[1]
        else:
            self.root.ids.main1.md_bg_color = self.colors[1]
            self.root.ids.btn1.md_bg_color = self.colors[3]
            self.root.ids.txt.text_color = self.colors[0]

test = q40()
test.run()