


class QuizBrain:
    def __init__(self, q_list) -> None:
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
        
        
    def next_question(self):
        if not self.has_next_question():
            return
        
        q_text = self.question_list[self.question_number].text
        self.question_number += 1
        return f"Q.{self.question_number}: {q_text}. (True/False) " 
    
    def has_next_question(self):
        return self.question_number < len(self.question_list)
    
    def check_answer(self, user_ans):
        curr_ans = self.question_list[self.question_number-1].answer
        if curr_ans.lower() == user_ans.lower():
            print('You got it right')
            self.score += 1
        else: 
            print('That\'s wrong')
            
        print(f'Current Score : {self.score}/{self.question_number}')
        print()
            
    