from tkinter import *
import csv
import random

window = Tk()
window.title("Flash Card")
window.geometry("600x400")
window.config(bg="#ffffff")

# Load questions and answers from CSV
questions = []
with open('questions.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        questions.append((row['Question'], row['Answer']))

current_index = 0
showing_question = True
known_cards = set()

def update_flashcard():
    global showing_question
    if len(known_cards) == len(questions):
        flashcard_label.config(text="All material known!")
        known_button.pack_forget()
        unknown_button.pack_forget()
    else:
        if showing_question:
            flashcard_label.config(text=questions[current_index][0])
        else:
            flashcard_label.config(text=questions[current_index][1])
        known_button.pack(side=LEFT, padx=10, pady=5)
        unknown_button.pack(side=RIGHT, padx=10, pady=5)

def flip_card():
    global showing_question
    showing_question = not showing_question
    update_flashcard()

def next_card():
    global current_index, showing_question
    if len(known_cards) < len(questions):
        current_index = (current_index + 1) % len(questions)
        while current_index in known_cards:
            current_index = (current_index + 1) % len(questions)
        showing_question = True
    update_flashcard()

def prev_card():
    global current_index, showing_question
    if len(known_cards) < len(questions):
        current_index = (current_index - 1) % len(questions)
        while current_index in known_cards:
            current_index = (current_index - 1) % len(questions)
        showing_question = True
    update_flashcard()

def shuffle_cards():
    global questions, current_index, showing_question, known_cards
    random.shuffle(questions)
    current_index = 0
    known_cards.clear()
    showing_question = True
    update_flashcard()

def mark_known():
    global current_index
    known_cards.add(current_index)
    next_card()

def mark_unknown():
    global current_index
    if current_index in known_cards:
        known_cards.remove(current_index)
    next_card()

frame = Frame(window, width=500, height=200, bd=2, relief="solid", bg="#D3D3D3")
frame.pack(pady=20)
frame.pack_propagate(False)

flashcard_label = Label(frame, text="Question?", font=("Alternate Gothic", 22), padx=30, pady=30, wraplength=450, bg="#D3D3D3")
flashcard_label.pack(expand=True)

button_font = ("Alternate Gothic", 16, "bold")

flip_button = Button(window, text="Flip", command=flip_card, font=button_font, padx=40, pady=20, bg="#ffffff")
flip_button.pack(pady=10)

next_button = Button(window, text="Next", command=next_card, font=button_font, padx=40, pady=20, bg="#ADD8E6", fg="#000000")
next_button.pack(side=RIGHT, padx=20, pady=20)

prev_button = Button(window, text="Previous", command=prev_card, font=button_font, padx=40, pady=20, bg="#ADD8E6", fg="#000000")
prev_button.pack(side=LEFT, padx=20, pady=20)

shuffle_button = Button(window, text="Shuffle", command=shuffle_cards, font=button_font, padx=40, pady=20, bg="#ffffff")
shuffle_button.pack(pady=10)

known_button = Button(frame, text="Known", command=mark_known, font=button_font, padx=20, pady=10, width=10, bg="#90EE90")
known_button.pack(side=LEFT, padx=10, pady=5)

unknown_button = Button(frame, text="Unknown", command=mark_unknown, font=button_font, padx=20, pady=10, width=10, bg="#FFB6C1")
unknown_button.pack(side=RIGHT, padx=10, pady=5)

update_flashcard()

window.mainloop()