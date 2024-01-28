import csv
import load
import renderer

def foundCity(grid, filename, xCell, yCell):
    print("Joo")
    row_index = yCell * 50 + xCell    
    with open(filename, 'r', newline='') as csvfile:
        rows = list(csv.reader(csvfile))
    if 0 <= row_index < len(rows):
        row = rows[row_index]
        if len(row) == 5:
            row[4] = '1'
            row[3] = '0'
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(rows)
    load.load_grid_from_csv(grid, 'save.csv')
    renderer.render_unit(grid, filename)