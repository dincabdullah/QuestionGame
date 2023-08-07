class QuizBrain():
    def __init__(self,question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0
    def next_question(self):
        current_question = self.question_list[self.question_number]
        answer = input("Q."+ str(self.question_number + 1) +" "+(current_question.text + "True/False? "))
        self.question_number +=1
        self.check_answer(self.question_number,answer,self.score)

    def still_have(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    def check_answer(self,question_num,answer,score):
        question = self.question_list[0]
        if question.answer == answer:
            score +=1
            print("You are right!")
        else:
            print("Your answer was false, the correct answer is : ",question.answer)
        self.score = score
        print("Current Score: ", score ,"/", question_num)
