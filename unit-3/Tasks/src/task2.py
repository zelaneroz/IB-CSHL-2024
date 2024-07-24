from kivymd.app import MDApp
class task2(MDApp):
    def build(self):
        return

    def set_input(self):
        self.value = int(self.root.ids.user_input.text)

    def to_bits(self):
        output = f"{self.value*8} Bit\n{self.value/125} Kilobits\n{self.value/125000} Megabits\n{self.value/125000000} Gigabit\n{self.value/125000000000} Terabit\n{self.value/(1.25*10*1*14)} Petabit\n{self.value/(1.25*10**17)} Exabit"
        self.root.ids.output.text = output

    def to_byte(self):
        output = f"{self.value/8} Byte\n{self.value/8000} Kilobyte\n{self.value/0.000008} Megabytes\n{self.value/0.000000008} Gigabytes\n{self.value/0.000000000008} Terabytes\n{self.value/0.000000000008} Petabytes\n{self.value/0.000000000008} Exabytes"
        self.root.ids.output.text = output

test = task2()
test.run()