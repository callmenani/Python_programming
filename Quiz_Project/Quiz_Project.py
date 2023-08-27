from data import question_data
class new_question:
    def __init__(self,texti,answeri):
        self.text = texti
        self.answer = answeri
    
question_bank = []

for items in question_data:
    question_text = items["text"]
    question_answer = items["answer"]
    new_q = new_question(question_text,question_answer) 
    question_bank.append(new_q)
    
class QuizBrain:
    def __init__(self,q_list):
        self.question_no = 0
        self.score = 0
        self.question_list = q_list
        
    def next_question(self):
        current_question = self.question_list[self.question_no]
        self.question_no += 1
        user_answer = input(f"Q.{self.question_no}: {current_question.text} (True/False): ").lower()
        self.check_answer(user_answer,current_question.answer)
    
    def remaining_questions(self):
        if self.question_no < len(self.question_list):
            return True
        else:
            return False
    def check_answer(self,user_answer,cq_answer):
        if user_answer == cq_answer.lower():
            print("Your right!")
            self.score +=  1
        else:
            print(f"Wrong Answer. Correct Answer is {cq_answer}")
        print(f"You score is {self.score}/{self.question_no}")
        
quiz = QuizBrain(question_bank)
while quiz.remaining_questions():
    quiz.next_question()
    
print("Quiz Completed !")
print(f"Your final score is {quiz.score}/{quiz.question_no}")