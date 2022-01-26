#: Defining class which will be used in multiple choice quiz

class Question:
    def __init__(self, prompt,answer):
        self.prompt = prompt
        self.answer = answer
