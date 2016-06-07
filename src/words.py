
class Words(object):
    def __init__(self, english, polish, example=""):
        self.english = english
        self.polish = polish
        self.example = example
    def english_translation(self):
        return self.english

    def polish_translation(self):
        return self.polish

    def example_show(self):
        return self.example

