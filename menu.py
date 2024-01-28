import tkinter as tk
root = tk.Tk()
def play_game():
    # Add code to start the game here
    root.destroy()
    import game
    print("Starting game...")

def exit_game():
    root.destroy()
def toggle_fullscreen():
    # Toggle fullscreen mode
    root.attributes("-fullscreen", not root.attributes("-fullscreen"))

def mute_window():
    # Mute the window (toggle the sound)
    # Implement your logic to mute/unmute the window
    print("Window muted/unmuted")

def show_options():
    options()
    print("Showing options...")
def main():
    # Destroy the previous frame and its widgets
    for widget in root.winfo_children():
        widget.destroy()
    # Create the Tkinter window 
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
def options():
    # Destroy the previous frame and its widgets
    for widget in root.winfo_children():
        widget.destroy()
        
    # Create a new frame for the options menu
    option_frame = tk.Frame(root)
    option_frame.pack(expand=True)

    # Create buttons for options
    fullscreen_button = tk.Button(option_frame, text="Toggle Fullscreen", command=toggle_fullscreen, width=20, height=3, font=("Helvetica", 16))
    mute_button = tk.Button(option_frame, text="Mute/Unmute", command=mute_window, width=20, height=3, font=("Helvetica", 16))
    back_button = tk.Button(option_frame, text="Back", command=main, width=20, height=3, font=("Helvetica", 16))

    # Pack buttons into the options menu frame
    fullscreen_button.grid(row=0, column=0, padx=10, pady=10)
    mute_button.grid(row=1, column=0, padx=10, pady=10)
    back_button.grid(row=2, column=0, padx=10, pady=10)