import tkinter as tk
import csv

def render_unit(grid, filename):
    with open(filename, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if len(row) == 4 and int(row[3]) == 1:
                x, y = int(row[0]), int(row[1])
                fill_color = "red"  # Adjust fill color as needed
                grid.setCell(x, y, fill=fill_color)
