import csv
from csvutils import getRowsFromCsv

def number_to_color(number):
    if number == 0:
        return 'blue' #Vesi
    elif number == 1:
        return 'yellow' #Aavikko
    elif number == 2:
        return 'green' #Ruoho ruutu
    elif number == 3:
        return 'grey' #Vuori
    elif number == 4:
        return 'cyan' #Spawnpoint
    else:
        return None  # Return None for unknown numbers

def load_grid_from_csv(grid, filename):
    reader = getRowsFromCsv(filename)
    for row in reader:
        if len(row) >= 3:  # Check if row has at least 3 elements
            x, y, number, *_ = map(int, row)  # Use * to handle extra elements
            color = number_to_color(number)
            if color is not None:
                grid.setCell(x, y, fill=color)

