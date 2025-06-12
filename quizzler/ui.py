THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx= 20, pady=20, bg=THEME_COLOR)
        
        #Score label
        self.score = Label(text="Score:0", bg=THEME_COLOR, fg="white")
        self.score.grid(row=0, column=1)
        
        #canvas for the questions
        self.canvas = Canvas(width=300, height= 250, bg="white")
        self.q_text = self.canvas.create_text(150, 125, text="Some Question Text", font=("Arial",20,"italic"), width=280)
        self.canvas.grid(row= 1, column=0, columnspan=2, pady=50)
        
        #True button
        true_img = PhotoImage(file="100DOC/quizzler/images/true.png")
        self.true_btn = Button(image=true_img, highlightthickness=0, bg=THEME_COLOR, bd=0, command=self.true_clicked)
        self.true_btn.grid(row=2, column=0)
        
        #False button
        false_img = PhotoImage(file="100DOC/quizzler/images/false.png")
        self.false_btn = Button(image=false_img, highlightthickness=0, bg=THEME_COLOR, bd=0, command=self.false_clicked)
        self.false_btn.grid(row=2, column=1)
        self.get_next_question()
        
        self.window.mainloop()
    
    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.q_text, text=q_text)
            self.score.config(text=f"Score:{self.quiz.score}")
        else:
            self.canvas.itemconfig(self.q_text, text="You've reached the end of the quiz")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")
            
        
    def check_answer(self, answer:str):
        is_right = self.quiz.check_answer(answer)
        self.give_feedback(is_right)
        
    def true_clicked(self):
        self.check_answer("true")
        
    def false_clicked(self):
        self.check_answer("false")
        
    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
            reset = self.window.after(1000, self.get_next_question)
            # self.window.after_cancel(reset)
        else:
            self.canvas.config(bg="red")
            reset = self.window.after(1000, self.get_next_question)
            # self.window.after_cancel(reset)
            