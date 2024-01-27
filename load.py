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
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            # Assuming the CSV format is x,y,number,unused
            if len(row) == 4:
                x, y, number, _ = map(int, row)
                color = number_to_color(number)
                if color is not None:
                    grid.setCell(x, y, fill=color)
