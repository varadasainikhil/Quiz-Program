from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

# Creating an array of question objects
for question in question_data:
    new_question = Question(question["question"], question["correct_answer"])
    question_bank.append(new_question)

# Creating an instance of the QuizBrain class
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the quiz !!")
print(f"Your final score is {quiz.score}/{len(quiz.question_list)}")
