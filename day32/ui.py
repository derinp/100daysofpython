from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        # Score Label
        self.score = Label(text="Score: 0", bg=THEME_COLOR)
        self.score.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, text="some text",
                                                     fill=THEME_COLOR,
                                                     font=("Arial", 20, "italic"),
                                                     width=280)

        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        # Buttons
        green_img = PhotoImage(file="images/true.png")
        self.green_button = Button(image=green_img, highlightthickness=0, command=self.green_pressed)
        self.green_button.grid(column=0, row=2)

        red_img = PhotoImage(file="images/false.png")
        self.red_button = Button(image=red_img, highlightthickness=0, command=self.red_pressed)
        self.red_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.config(bg="white")
            self.canvas.itemconfig(self.question_text, text="No more questions\n"
                                                            f"Final score is {self.quiz.score}/10")

    def green_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def red_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
