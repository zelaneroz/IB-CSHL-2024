from kivymd.app import MDApp

class q41(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.turn = "X"
    def build(self):
        return

    #Define who's turn

    def press(self, btn):
        if self.turn=='X':
            btn.text = "X"
            btn.color_disabled=(252, 186, 3)
            btn.md_bg_color_disabled= [0, 0, 102, 100]
            btn.disabled = True
            self.root.ids.player.text = "It is O's turn!"
            self.turn = 'O'
        else:
            btn.text = "O"
            btn.md_bg_color_disabled= [102, 0, 102, 100]
            btn.disabled = True
            self.root.ids.player.text = "It is X's turn!"
            self.turn = 'X'

test = q41()
test.run()

#PSEUDOCODE

#everytime it's someone's turn:
    #change name
    #Let any button, unless already been pressed, be pressed
    #if pressed, change color
    #then next turn

#how to make it every person's turn:


# - MDBoxLayout - all contents
# - 3x3 box
# - MDLabel - Tic Tac Toe by student_name
# - MDLabel - It is X's turn
# - MDBoxLayout - vertical; 1 width; .3 height8
#     - MDBoxLayout - horizontal; width is a .3
#     - color of each raised button is first green.
#
# - My Add-ons (HL)
#     - yellow & red for different turns;
#     - change name of 2nd MDLabel for every turn.
#     -

