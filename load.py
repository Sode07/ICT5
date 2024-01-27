import csv

def number_to_color(number):
    if number == 0:
        return 'blue'
    elif number == 1:
        return 'yellow'
    elif number == 2:
        return 'green'
    elif number == 3:
        return 'grey'
    else:
        return None  # Return None for unknown numbers

def load_grid_from_csv(grid, filename):
    with open(filename, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for y, row in enumerate(reader):
            for x, number in enumerate(row):
                color = number_to_color(int(number))
                if color is not None:
                    grid.setCell(x, y, fill=color)