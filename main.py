from question_model import CreateQuestion
from data import question_data
from quiz_brain import QuizBrain
question_list = []
for element in question_data:
    text = element["text"]
    answer = element["answer"]
    question = CreateQuestion(text,answer)
    question_list.append(question)

#print(question_list[0].text)

quiz_brain = QuizBrain(question_list)

while quiz_brain.still_have():
    quiz_brain.next_question()

print("\n\nYou finished the quiz, here is the result!")
print("Your final score is : ", quiz_brain.score, "/" ,len(question_list))