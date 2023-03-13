class QuizBrain:
    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0
        self.score = 0

    def next_question(self):
        # current question is a variable that contains the current question object
        current_question = self.question_list[self.question_number]
        # the q_text is the text of the current question
        q_text = current_question.text
        # the q_answer is the answer of the current question
        q_answer = current_question.answer
        # This is the actual print statement that is shown to the user
        answer = input(f"Q.{self.question_number + 1}. {q_text} (True/False) ?:")
        # To check the answer
        self.check_answers(answer, q_answer)
        self.question_number += 1

    def still_has_questions(self):
        return self.question_number < len(self.question_list)  # This will return a boolean value based on the values

    def check_answers(self, answer, q_answer):
        if answer.lower() == q_answer.lower():
            self.score += 1
            print("You got it right !")
            print(f"Your score is {self.score}/{self.question_number + 1}")
        else:
            print("You got it wrong !!")
            print(f"The correct answer was {q_answer}")
        print("\n")
