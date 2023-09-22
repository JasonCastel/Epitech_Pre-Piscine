import tkinter as tk

# Create a Tkinter window
window = tk.Tk()
window.title("Game GUI")

# Create a canvas to draw the game graphics (if needed)
canvas = tk.Canvas(window, width=200, height=50)
canvas.pack()

# Initialize game variables
score = 0
time_remaining = 60  # in seconds
life = 3
inventory = ["Item 1", "Item 2", "Item 3"]

# Function to update the time display
def update_time():
    global time_remaining
    if time_remaining > 0:
        time_remaining -= 1
        time_label.config(text=f"Time: {time_remaining} sec")
        window.after(1000, update_time)
    else:
        # Handle game over when time runs out
        game_over_label.config(text="Game Over!")

# Function to update the score
def update_score(points):
    global score
    score += points
    score_label.config(text=f"Score: {score}")

# Function to update the life bar
def update_life_bar():
    life_bar.config(text=f"Life: {life * '❤️'}")

# Function to open the game menu
def open_menu():
    menu_window = tk.Toplevel(window)
    menu_window.title("Game Menu")

    # Add menu options and buttons as needed
    menu_label = tk.Label(menu_window, text="Game Menu")
    menu_label.pack()

    resume_button = tk.Button(menu_window, text="Resume Game", command=menu_window.destroy)
    resume_button.pack()

    quit_button = tk.Button(menu_window, text="Quit Game", command=window.quit)
    quit_button.pack()

# Score label
score_label = tk.Label(window, text=f"Score: {score}")
score_label.pack()

# Time label
time_label = tk.Label(window, text=f"Time: {time_remaining} sec")
time_label.pack()
update_time()

# Life bar label
life_bar = tk.Label(window, text=f"Life: {life * '❤️'}")
life_bar.pack()

# Inventory label
inventory_label = tk.Label(window, text="Inventory:")
inventory_label.pack()

# Inventory listbox
inventory_listbox = tk.Listbox(window)
for item in inventory:
    inventory_listbox.insert(tk.END, item)
inventory_listbox.pack()

# Menu button
menu_button = tk.Button(window, text="Menu", command=open_menu)
menu_button.pack()

# Game over label (initially hidden)
game_over_label = tk.Label(window, text="", font=("Helvetica", 20))
game_over_label.pack()
game_over_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Example usage: Update the score when a button is clicked
def increase_score():
    update_score(10)

score_button = tk.Button(window, text="Increase Score", command=increase_score)
score_button.pack()

# Example usage: Update the life bar when a button is clicked
def decrease_life():
    global life
    if life > 0:
        life -= 1
        update_life_bar()
    if life == 0:
        game_over_label.config(text="Game Over!")

life_button = tk.Button(window, text="Decrease Life", command=decrease_life)
life_button.pack()

# Start the Tkinter main loop
window.mainloop()
