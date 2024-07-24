class WordCounter:
    def __init__(self,text:str):
        self.text = text
    def count_words(self):
        y = self.text.split(' ')
        return y
    def get_results(self):
        x={}
        return x

text = "This is a test text. It contains some words that will be counted."
counter = WordCounter(text)
print(counter.count_words())
#result = counter.get_results()