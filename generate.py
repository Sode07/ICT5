import noise
import random
from tkinter import Tk, Button
from hexagonal_grid import HexagonalGrid
import csv
import turn_handler
from csvutils import getRowsFromCsv

scaleX = 0.05*random.uniform(0.9,1.1)
scaleY = 0.05*random.uniform(0.1,0.5)
mountain = -0.8
desert = 0.3
grass = 0.2

def Continents():
    return
def Desert():
    return
def Hills():
    return
def Ocean():
    return

def get_tile_content_from_csv(filename, x, y):
    reader = getRowsFromCsv(filename)
    for row in reader:
            # Assuming the CSV format is x,y,number
        if len(row) >= 5:  # Check if row has at least 5 elements
            csv_x, csv_y, number, *_ = map(int, row)  # Use * to handle extra elements
            if csv_x == x and csv_y == y:
                return number
    # Return None if the tile is not found
    return None

def spawn_unit(filename):
    check_x =1
    check_y =13
    while True: #Hei Sallasmaa
        tile_content = get_tile_content_from_csv(filename, check_x, check_y)
        if tile_content == 2:
            print(check_y)
            row_index = check_y * 50 + check_x - 1
            rows = getRowsFromCsv(filename)
            if 0 <= row_index < len(rows):
                row = rows[row_index]
                if len(row) >= 5:
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
def SetSpawn(filename):
    check_x =1
    check_y =13
    while True:
        tile_content = get_tile_content_from_csv(filename, check_x, check_y)
        if tile_content == 2:
            print(check_y)
            row_index = check_y * 50 + check_x - 1    
            rows = getRowsFromCsv(filename)
            if 0 <= row_index < len(rows):
                row = rows[row_index]
                if len(row) >= 5:
                    row[2] = '4'
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
                writer.writerow([x, y, number, 0, 0, 0])  # Pass individual elements



# Color mapping based on Perlin noise value and surrounding tiles
def color_from_noise(x, y):
    noise_value = (noise.perlin(x * scaleX, y * scaleY, 500, 500)-0.33)*2
    # Return the original color based on noise value
    if noise_value < mountain:
        return 'grey'
    elif noise_value < grass:
        return 'green'
    elif noise_value < desert:
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
            color = color_from_noise(x, y)  # Pass the grid parameter
            grid.setCell(x, y, fill=color)
    save_grid_to_csv(grid, saveFile)

    spawn_unit(saveFile)
    SetSpawn(saveFile)
    turn_handler.write_current_turn('save.csv', 1)
    tk.mainloop()
