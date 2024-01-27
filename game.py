from tkinter import Tk
from hexagonal_grid import HexagonalGrid
from load import load_grid_from_csv

# Create Tkinter window
tk = Tk()

# Create HexagonalGrid instance
grid = HexagonalGrid(tk, scale=20, grid_width=50, grid_height=25)
grid.grid(row=0, column=0, padx=5, pady=5)

# Load grid from CSV using grid_loader
load_grid_from_csv(grid, 'grid_colors.csv')

# Run Tkinter event loop
tk.mainloop()
