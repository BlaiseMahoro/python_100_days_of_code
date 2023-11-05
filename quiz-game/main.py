
from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

def create_quiz():
    question_bank = [Question(q['text'], q['answer']) for q in question_data]
    quiz = QuizBrain(question_bank)
    return quiz


def main():
    
    quiz = create_quiz()
    
    while quiz.has_next_question():
        nextQ = quiz.next_question()
        user_ans = input(nextQ)
        quiz.check_answer(user_ans)
    print('You\'ve completed the quiz')
    print(f'Your final score is {quiz.score}/{quiz.question_number}')
    
    
main()




