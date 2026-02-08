"""For all questioning and quizzing functionality """
class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0 # ques number in ques list start as 0. so the question_number attribute initial as 0
        self.question_list = q_list #pass it from the new_question object that from the question_bank
        self.score = 0 # for keep track of score and starts withe zero

    def next_question(self):
        current_question = self.question_list[self.question_number] # question_list[0]
        self.question_number += 1
        # input(f"Q.{self.question_number}: {current_question.text} (True/False):") save this separate variable
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False):")
        self.check_answer(user_answer,current_question.answer)
        # for check_answer passing the value user answer and current_question.answer = represents exacts answer in data
        # current_question.text = "shows questions"

    def check_answer(self , user_answer, correct_answer):
        """Function to check if the user answered correctly increase the score"""
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("you got it! right answer!")
        else:
            print("that's wrong answer!")

        print(f" The Correct Answer is {correct_answer}")
        print(f" Your Current Score is {self.score}/{self.question_number}")

    def still_has_questions(self):
        """function return true if question_number has less than
        a length of question_list"""
        # len(self.question_list)
        # if self.question_number < len(self.question_list):
        #     return True
        # else:
        #     return False
        return self.question_number < len(self.question_list)

