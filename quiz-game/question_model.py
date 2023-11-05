

class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer
        
        
    def __str__(self) -> str:
        return 'Text: {0} - Answer: {1}'.format(self.text, self.answer)