import noise
import random
from tkinter import Tk, Button
from hexagonal_grid import HexagonalGrid
import csv

def color_to_number(color):
    if color == 'blue':
        return 0
    elif color == 'yellow':
        return 1
    elif color == 'green':
        return 2
    elif color == 'grey':
        return 3
    else:
        return -1  # Return -1 for unknown colors

def save_grid_to_csv(grid, filename):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for y in range(grid_height):
            row = []
            for x in range(grid_width):
                color = grid.getFill(x, y)
                number = color_to_number(color)
                row.append(number)
            writer.writerow(row)


# Color mapping based on Perlin noise value and surrounding tiles
def color_from_noise(x, y, grid):
    scale = 0.05  # Adjust the scale to control the noise frequency
    noise_value = (noise.perlin(x * scale*random.uniform(0.9,1.1), y * scale*random.uniform(0.1,0.5), 500, 500)-0.33)*2
    # Return the original color based on noise value
    if noise_value < -0.8:
        return 'grey'
    elif noise_value < 0.2:
        return 'green'
    elif noise_value < 0.3:
        return 'yellow'
    else:
        return 'blue'


if __name__ == "__main__":
    tk = Tk()

    scale = 20  # Adjust the scale of the hexagons as needed
    grid_width = 50  # Number of hexagons wide
    grid_height = 25  # Number of hexagons tall

    grid = HexagonalGrid(tk, scale, grid_width, grid_height)
    grid.grid(row=0, column=0, padx=5, pady=5)

    def correct_quit(tk):
        tk.destroy()
        tk.quit()

    quit_button = Button(tk, text="Quit", command=lambda: correct_quit(tk))
    quit_button.grid(row=1, column=0)

    for x in range(grid_width):
        for y in range(grid_height):
            color = color_from_noise(x, y, grid)  # Pass the grid parameter
            grid.setCell(x, y, fill=color)
    save_grid_to_csv(grid, 'grid_colors.csv')

    tk.mainloop()
