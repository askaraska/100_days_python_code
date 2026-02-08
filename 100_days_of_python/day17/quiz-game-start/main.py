#step1: Our goal is create a question bank of question object
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

"""Write a for loop to iterate through the question data."""
question_bank = [] # which is going to be list of question object
"""create a Question Object from entry in question_data."""
for question in question_data:
    question_text = question["text"]  # question data in question. so question is act as dict
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)
# print(question_bank)
# print(question_bank[0].text)
quiz = QuizBrain(question_bank) # we create a new quiz(obj) from QuizBrain class

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your Final Score is: {quiz.score}/{quiz.question_number}")