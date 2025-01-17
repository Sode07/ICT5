import tkinter as tk
from csvutils import getRowsFromCsv

def render_unit(grid, filename):
    reader = getRowsFromCsv(filename)
    for row in reader:
        if len(row) >= 5 and int(row[3]) == 1:
            x, y = int(row[0]), int(row[1])
            fill_color = "red"  # Adjust fill color as needed
            grid.setCell(x, y, fill=fill_color)
def render_city(grid, filename):
    reader = getRowsFromCsv(filename)
    for row in reader:
        if len(row) >= 5 and int(row[4]) > 0:
            x, y = int(row[0]), int(row[1])
            fill_color = "black"  # Adjust fill color as needed
            grid.setCell(x, y, fill=fill_color)