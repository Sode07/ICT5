import tkinter as tk
import city
import turn_handler as TH

def baseUI(root, filename):
    button_frame = tk.Frame(root)
    button_frame.grid(row=1, column=1)  # Example row and column numbers

    EndTurnButton = tk.Button(button_frame, text="End Turn", command=lambda: TH.endTurn(filename))
    EndTurnButton.grid(row=0, column=0, padx=10, pady=10)
    
def settlerUI(root, grid, filename, xCell, yCell):
    button_frame = tk.Frame(root)
    button_frame.grid(row=1, column=1)  # Example row and column numbers

    FoundCityButton = tk.Button(button_frame, text="Found City", command=lambda: city.foundCity(grid, filename, xCell, yCell, FoundCityButton, root))

    FoundCityButton.grid(row=0, column=0, padx=10, pady=10)

def cityUI(root, grid, filename):
    button_frame = tk.Frame(root)
    button_frame.grid(row=1, column=1)  # Example row and column numbers

    buttons_to_destroy = []

    Civilian = tk.Button(button_frame, text="Civilian", command=lambda: city.ProduceUnit(0, buttons_to_destroy, grid, filename, root))
    EndTurnButton = tk.Button(button_frame, text="End Turn", command=lambda: TH.endTurn(filename))

    EndTurnButton.grid(row=0, column=1, padx=10, pady=10)
    Civilian.grid(row=0, column=0, padx=10, pady=10)

    buttons_to_destroy.extend([Civilian])

    print("City selected")
