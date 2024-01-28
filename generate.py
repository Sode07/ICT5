import noise
import random
from tkinter import Tk, Button
from hexagonal_grid import HexagonalGrid
import csv

def get_tile_content_from_csv(filename, x, y):
    with open(filename, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            # Assuming the CSV format is x,y,number
            if len(row) == 5:
                csv_x, csv_y, number, _, __ = map(int, row)
                if csv_x == x and csv_y == y:
                    return number
    # Return None if the tile is not found
    return None
def spawn_unit(filename):
    check_x =5
    check_y =13
    while True:
        tile_content = get_tile_content_from_csv(filename, check_x, check_y)
        if tile_content == 2:
            print(check_y)
            row_index = check_y * 50 + check_x - 1    
            with open(filename, 'r', newline='') as csvfile:
                rows = list(csv.reader(csvfile))
            if 0 <= row_index < len(rows):
                row = rows[row_index]
                if len(row) == 5:
                    row[2] = '2'
                    row[3] = '1'
            with open(filename, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerows(rows)

            return()
        elif check_y > 1:
            check_y -=1
        else:
            check_y = 25
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
        return None  # Return None for unknown colors

def save_grid_to_csv(grid, filename):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for y in range(grid_height):
            for x in range(grid_width):
                color = grid.getFill(x, y)
                number = color_to_number(color)
                writer.writerow([x, y, number, 0, 0])  # Pass individual elements



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
    
    saveFile='save.csv'
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
    save_grid_to_csv(grid, saveFile)

    spawn_unit(saveFile)

    tk.mainloop()
