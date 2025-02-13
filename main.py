from tkinter import *

window = Tk()
window.title("Flash Card")
window.geometry("600x400")

def flip_card():
    if flashcard1_question.cget("text") == "Question?":
        flashcard1_question.config(text="Answer?")
    else:
        flashcard1_question.config(text="Question?")

flashcard1_question = Button(window,
                   text = "Question?",
                   font=("Arial", 22),
                   padx=30, pady=30,
                   command=flip_card
                   )

flashcard1_question.pack()


window.mainloop()