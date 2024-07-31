from question_model import Question
# from data import question_data
from quiz_brain import QuizBrain
from ui import UserInterface
import requests

response = requests.get(url='https://opentdb.com/api.php?amount=10&category=18&difficulty=medium&type=boolean')
response.raise_for_status()

data = response.json()['results']

question_bank = []
for question in data:
    question_text = question['question']
    quesiton_answer = question['correct_answer']
    new_question = Question(question_text, quesiton_answer)
    question_bank.append(new_question)

# question_bank = []
# for question in question_data:
#     question_text = question["question"]
#     question_answer = question["correct_answer"]
#     new_question = Question(question_text, question_answer)
#     question_bank.append(new_question)


quiz = QuizBrain(question_bank)
quiz_ui = UserInterface(quiz)

# while quiz.still_has_questions():
#     quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
