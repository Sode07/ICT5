import tkinter as tk

def play_game():
    # Add code to start the game here
    print("Starting game...")

def exit_game():
    root.destroy()

def show_options():
    # Add code to show options menu
    print("Showing options...")

# Create the Tkinter window
root = tk.Tk()
root.attributes("-fullscreen", True)  # Set full screen

# Create a frame for the buttons
button_frame = tk.Frame(root)
button_frame.place(relx=1.0, rely=1.0, anchor='se', x=-20, y=-20)

# Create buttons
play_button = tk.Button(button_frame, text="Play", command=play_game, width=20, height=3, font=("Helvetica", 16))
exit_button = tk.Button(button_frame, text="Exit", command=exit_game, width=20, height=3, font=("Helvetica", 16))
options_button = tk.Button(button_frame, text="Options", command=show_options, width=20, height=3, font=("Helvetica", 16))

# Pack buttons into the frame
play_button.grid(row=0, column=0, padx=10, pady=10, sticky='ew')
options_button.grid(row=1, column=0, padx=10, pady=10, sticky='ew')
exit_button.grid(row=2, column=0, padx=10, pady=10, sticky='ew')

# Run the Tkinter event loop
root.mainloop()
