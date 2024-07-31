from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class UserInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.score = 0
        self.quiz = quiz_brain
        self.window =  Tk()
        self.window.title('Quizzler App')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score_label = Label(text='Score: 0', bg=THEME_COLOR, fg='white', font=('Arial', 20, 'bold'))
        self.score_label.grid(row=0, column=0)
        self.canvas = Canvas(width=300, height=250, bg='white')
        self.question_text = self.canvas.create_text(150, 125, width=280, text='A question', fill=THEME_COLOR, font=('Arial', 20, 'italic'))
        self.canvas.grid(row=1, column=0, columnspan=2)
        true_image = PhotoImage(file='images/true.png')
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.click_true)
        self.true_button.grid(row=2, column=0)
        false_image = PhotoImage(file='images/false.png')
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.click_false)
        self.false_button.grid(row=2, column=1)
        self.get_next_question()
        self.window.mainloop()
    def get_next_question(self):
        self.canvas.config(background='white')
        if self.quiz.still_has_questions():
            self.score_label.config(text=f'Score: {self.score}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text='Thank you for playing!')
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')
    def click_true(self):
        correct = self.quiz.check_answer(user_answer='true')
        self.getFeedback(correct)
    def click_false(self):
        correct = self.quiz.check_answer(user_answer='false')
        self.getFeedback(correct)
    def getFeedback(self, correct):
        if correct:
            self.score+=1
            self.canvas.config(background='green')
        elif not correct:
            self.canvas.config(background='red')
        self.window.after(1000, self.get_next_question)
