from tkinter import Tk
from hexagonal_grid import HexagonalGrid
import load
import renderer
import movement
filename = "save.csv"


# Create Tkinter window
tk = Tk()

# Create HexagonalGrid instance
grid = HexagonalGrid(tk, scale=20, grid_width=50, grid_height=25)
grid.grid(row=0, column=0, padx=5, pady=5)

# Load grid from CSV using grid_loader
load.load_grid_from_csv(grid, 'save.csv')

renderer.render_unit(grid, filename)
# Bind the canvas to the select_unit function
grid.bind("<Button-1>", lambda event: movement.select_unit(event, grid, filename))
# Bind the right-click event to the move_unit function
grid.bind("<Button-3>", lambda event: movement.move_unit(event, grid, filename))
# Run Tkinter event loop
tk.mainloop()
