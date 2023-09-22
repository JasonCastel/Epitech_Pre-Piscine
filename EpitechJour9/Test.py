import random
import datetime
import tkinter as tk
from tkinter import messagebox

def mot_fichier(nomFichier):
    with open(nomFichier, 'r') as fichier:
        liste = [ligne.strip() for ligne in fichier]
        return liste

def jeux(s, window):
    result = ['_'] * len(s)
    guesses = set()
    score = 0

    canvas = tk.Canvas(window, width=200, height=200)
    canvas.pack()
    canvas.create_line(50, 180, 150, 180, width=2)  # Base
    canvas.create_line(100, 180, 100, 20, width=2)  # Pole
    canvas.create_line(100, 20, 150, 20, width=2)   # Beam
    canvas.create_line(150, 20, 150, 50, width=2)   # Rope

    def draw_head():
        canvas.create_oval(130, 50, 170, 90, width=2)  # Head

    def draw_body():
        canvas.create_line(150, 90, 150, 140, width=2)  # Body

    def draw_left_arm():
        canvas.create_line(150, 100, 120, 130, width=2)  # Left Arm

    def draw_right_arm():
        canvas.create_line(150, 100, 180, 130, width=2)  # Right Arm

    def draw_left_leg():
        canvas.create_line(150, 140, 130, 170, width=2)  # Left Leg

    def draw_right_leg():
        canvas.create_line(150, 140, 170, 170, width=2)  # Right Leg

    def draw_hangman():
        draw_functions = [draw_head, draw_body, draw_left_arm, draw_right_arm, draw_left_leg, draw_right_leg]
        for i in range(score):
            draw_functions[i]()

    def update_hangman():
        nonlocal score
        if score < 6:
            draw_hangman()
        else:
            messagebox.showinfo("Game Over", f"You have run out of attempts. The word was '{s}'.")
            update_score(score)
            window.destroy()

    def guess_letter(letter, letter_buttons):
        nonlocal score
        if letter in guesses:
            messagebox.showinfo("Duplicate Guess", f"You have already guessed {letter}.")
            return
        guesses.add(letter)
        guessed_letters_label.config(text=f"Guessed Letters: {' '.join(guesses)}")
        if letter in s:
            for i in range(len(s)):
                if s[i] == letter:
                    result[i] = letter
            word_label.config(text=" ".join(result))
            if "_" not in result:
                messagebox.showinfo("Congratulations", f"You have guessed the word '{s}' with {score} wrong guesses.")
                update_score(score)
                window.destroy()
        else:
            score += 1
            update_hangman()
        
        
        letter_buttons[ord(letter) - ord('a')].config(state='disabled')
        letter_buttons[ord(letter) - ord('a')].pack_forget()

    def update_score(score):
        global old_score
        old_score = read_old_score(file_path)
        if old_score is None or score < old_score:
            with open(file_path, 'w') as file:
                new_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                file.write(f"Le meilleur score est: {score} (mise à jour le {new_date})")

    word_label = tk.Label(window, text=" ".join(result), font=("Helvetica", 20))
    word_label.pack()

    letter_buttons_frame = tk.Frame(window)
    letter_buttons_frame.pack()
    letter_buttons = []

    for letter in 'abcdefghijklmnopqrstuvwxyz':
        letter_button = tk.Button(letter_buttons_frame, text=letter, command=lambda l=letter: guess_letter(l, letter_buttons))
        letter_buttons.append(letter_button)

    for letter_button in letter_buttons:
        letter_button.grid(row=0, column=ord(letter_button['text']) - ord('a'), padx=5, pady=5)

    guessed_letters_label = tk.Label(window, text="Guessed Letters:")
    guessed_letters_label.pack()

def read_old_score(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read().strip()
            if content:
                return int(content.split(':')[1].strip().split()[0])
            else:
                return None
    except FileNotFoundError:
        return None
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return None

def start_game():
    global metrouve
    metrouve = random.choice(mottrouver).lower()
    root = tk.Tk()
    root.title("Hangman Game")
    jeux(metrouve, root)
    root.mainloop()

def quit_game():
    window.destroy()

file_path = r"C:\Users\jason\python\test.txt"
old_score = read_old_score(file_path)

window = tk.Tk()
window.title("Pendu Game")

start_button = tk.Button(window, text="Start Game", command=start_game)
quit_button = tk.Button(window, text="Quit Game", command=quit_game)

start_button.pack()
quit_button.pack()

mottrouver = mot_fichier(r"C:\Users\jason\python\EpitechJour9\ods4.txt")

window.mainloop()
