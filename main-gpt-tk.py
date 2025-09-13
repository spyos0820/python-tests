import random
import tkinter as tk
from tkinter import messagebox

# -------------------------------
# Globale variabelen
# -------------------------------
sentence = ""
sentence_clean = ""
words = []
words_clean = []

current_number_10 = None
current_number_100 = None

# -------------------------------
# Functies
# -------------------------------
def new_sentence():
    global sentence, sentence_clean, words, words_clean
    sentence = random.choice(subjects) + " " + random.choice(verbs) + " " + random.choice(objects) + "."
    sentence_clean = sentence.lower().strip(".,?!")
    words = sentence.split()
    words_clean = [w.strip(".,!?").lower() for w in words]
    if debug.get():
        output_text.set(f"[DEBUG] The sentence is: {sentence_clean}")
    else:
        output_text.set(f"📝 The sentence contains {len(words)} words.")

def guess_word():
    guess = input_text.get().lower().strip()
    if guess == "exit":
        messagebox.showinfo("Game", f"The sentence was: {sentence}")
        return
    if guess == sentence_clean:
        messagebox.showinfo("🎉 Success!", f"You guessed the whole sentence!\n{sentence}")
        new_sentence()
    elif guess in words_clean:
        pos = words_clean.index(guess) + 1
        output_text.set(f"✅ '{guess}' is in the sentence at position {pos}")
    else:
        hint = random.choice(words_clean) if debug.get() else "🤔 Use your imagination!"
        output_text.set(f"❌ '{guess}' is not in the sentence. Hint: {hint}")
    input_text.set("")

def new_number(max_number):
    global current_number_10, current_number_100
    if max_number == 10:
        current_number_10 = random.randrange(1, 11)
        if debug.get():
            output_text.set(f"[DEBUG] Number: {current_number_10}")
        else:
            output_text.set("Guess the number between 1-10!")
    else:
        current_number_100 = random.randrange(1, 101)
        if debug.get():
            output_text.set(f"[DEBUG] Number: {current_number_100}")
        else:
            output_text.set("Guess the number between 1-100!")

def guess_number(max_number):
    guess_str = input_text.get().strip()
    if guess_str.lower() == "exit":
        output_text.set("Game stopped.")
        input_text.set("")
        return
    try:
        guess = int(guess_str)
    except ValueError:
        output_text.set("⚠️ Please enter a valid number.")
        return

    number = current_number_10 if max_number == 10 else current_number_100

    if guess < number:
        output_text.set("⬆️ Higher!")
    elif guess > number:
        output_text.set("⬇️ Lower!")
    else:
        output_text.set("🎉 You guessed right!!!")
        new_number(max_number)  # alleen nieuw nummer genereren als het geraden is

    input_text.set("")

# -------------------------------
# GUI Setup
# -------------------------------
root = tk.Tk()
root.title("🎮 Python Guessing Game")
root.geometry("500x450")
root.configure(bg="#f0f8ff")  # lichte blauwe achtergrond

# Debug mode
debug = tk.BooleanVar()
debug.set(True)

# Tekstvariabelen
output_text = tk.StringVar()
input_text = tk.StringVar()

# Layout
tk.Label(root, text="🎲 Python Guessing Game", font=("Arial", 20, "bold"), fg='black', bg="#f0f8ff").pack(pady=10)
tk.Checkbutton(root, text="Debug mode", variable=debug, bg="#f0f8ff", fg="black", font=("Arial", 12)).pack()
tk.Entry(root, textvariable=input_text, font=("Arial", 14), bg="#f0f8ff", fg="black", width=30, justify="center").pack(pady=10)
tk.Label(root, textvariable=output_text, wraplength=450, font=("Arial", 14), fg="black", bg="#f0f8ff").pack(pady=10)

# Buttons
button_frame = tk.Frame(root, bg="#f0f8ff")
button_frame.pack(pady=10)

tk.Button(button_frame, text="Guess Word/Sentence", command=guess_word, bg="#90ee90", fg="black", font=("Arial", 12, "bold"), width=20).grid(row=0, column=0, padx=5, pady=5)
tk.Button(button_frame, text="Guess Number 1-10", command=lambda: guess_number(10), bg="#ffcccb", fg="black", font=("Arial", 12, "bold"), width=20).grid(row=1, column=0, padx=5, pady=5)
tk.Button(button_frame, text="Guess Number 1-100", command=lambda: guess_number(100), bg="#add8e6", fg="black", font=("Arial", 12, "bold"), width=20).grid(row=2, column=0, padx=5, pady=5)
tk.Button(button_frame, text="New Sentence", command=new_sentence, bg="#ffff99", fg="black", font=("Arial", 12, "bold"), width=20).grid(row=3, column=0, padx=5, pady=5)
tk.Button(button_frame, text="Exit", command=root.quit, bg="#d3d3d3", fg="black", font=("Arial", 12, "bold"), width=20).grid(row=4, column=0, padx=5, pady=5)

# -------------------------------
# Data
# -------------------------------
subjects = ["The cat", "My friend", "A programmer", "The teacher", "An astronaut"]
verbs = ["eats", "writes", "builds", "finds", "sees"]
objects = ["a book", "the code", "a pizza", "the answer", "a spaceship"]

# Start
new_sentence()
new_number(10)
new_number(100)
root.mainloop()
