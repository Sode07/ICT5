from tkinter import Tk, Button
from hexagonal_grid import HexagonalGrid
import random

if __name__ == "__main__":
    tk = Tk()

    scale = 20  # Adjust the scale of the hexagons as needed
    grid_width = 50  # Number of hexagons wide
    grid_height = 25  # Number of hexagons tall

    colors = ['yellow', 'green', 'grey', 'blue']  # Define colors to choose from

    grid = HexagonalGrid(tk, scale=scale, grid_width=grid_width, grid_height=grid_height)
    grid.grid(row=0, column=0, padx=5, pady=5)

    def correct_quit(tk):
        tk.destroy()
        tk.quit()

    quit_button = Button(tk, text="Quit", command=lambda: correct_quit(tk))
    quit_button.grid(row=1, column=0)

    for x in range(grid_width):
        for y in range(grid_height):
            color = random.choice(colors)  # Choose a random color from the list
            grid.setCell(x, y, fill=color)  # Fill the cell with the chosen color

    tk.mainloop()
