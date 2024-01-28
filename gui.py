import tkinter as tk
import city

def settlerUI(root, grid, filename, xCell, yCell):
    button_frame = tk.Frame(root)
    button_frame.grid(row=1, column=1)  # Example row and column numbers

    FoundCityButton = tk.Button(button_frame, text="Found City", command=city.foundCity(grid, filename, xCell, yCell))
    FoundCityButton.grid(row=0, column=0, padx=10, pady=10)
