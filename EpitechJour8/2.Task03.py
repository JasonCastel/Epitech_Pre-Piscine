import tkinter as tk

# Create a Tkinter window
window = tk.Tk()
window.title("Stickman Animation")

# Create a canvas to draw on
canvas = tk.Canvas(window, width=200, height=300)
canvas.pack()

# Initialize the initial arm positions
left_arm_y = 120
right_arm_y = 120
arm_direction = 1  # 1 for moving up, -1 for moving down

# Function to animate the stickman
def animate_stickman():
    global left_arm_y, right_arm_y, arm_direction

    # Clear the canvas
    canvas.delete("all")

    # Update arm positions
    left_arm_y += 5 * arm_direction
    right_arm_y -= 5 * arm_direction

    # If arms reach certain positions, change direction
    if left_arm_y <= 115 or left_arm_y >= 125:
        arm_direction *= -1

    # Draw the stickman with updated arm positions
    canvas.create_oval(75, 50, 125, 100, outline="black", width=2)
    canvas.create_line(100, 100, 100, 200, fill="black", width=2)
    canvas.create_line(100, left_arm_y, 60, 160, fill="black", width=2)
    canvas.create_line(100, right_arm_y, 140, 160, fill="black", width=2)
    canvas.create_line(100, 200, 60, 250, fill="black", width=2)
    canvas.create_line(100, 200, 140, 250, fill="black", width=2)
    canvas.create_text(100, 30, text="Stickman", fill="black", font=("Arial", 12))

    # Repeat the animation after a delay
    window.after(100, animate_stickman)

# Start the animation
animate_stickman()

# Start the Tkinter main loop
window.mainloop()
