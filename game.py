import tkinter as tk
from hexagonal_grid import HexagonalGrid
import load
import renderer
import movement
import gui
import turn_handler
filename = "save.csv"

# Create Tkinter window
root = tk.Tk()
"""root.attributes('-fullscreen', True)"""
# Create HexagonalGrid instance
grid = HexagonalGrid(root, scale=20, grid_width=50, grid_height=25)
grid.grid(row=0, column=0, padx=5, pady=5)

# Load grid from CSV using grid_loader
load.load_grid_from_csv(grid, filename)
gui.baseUI(root, filename)
renderer.render_unit(grid, filename)
renderer.render_city(grid, filename)
# Bind the canvas to the select_unit function
grid.bind("<Button-1>", lambda event: movement.select_unit(event, grid, filename, root))
# Bind the right-click event to the move_unit function
grid.bind("<Button-3>", lambda event: movement.move_unit(event, grid, filename, turn_handler.get_current_turn(filename)))
# Run Tkinter event loop
root.mainloop()
