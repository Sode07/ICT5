import csv
import load
import renderer
import gui
import production
import turn_handler
from csvutils import getRowsFromCsv

def foundCity(grid, filename, xCell, yCell, button, root):
    print("Joo")
    row_index = grid.getIndexFromXY(xCell, yCell) 
    rows = getRowsFromCsv(filename)
    if 0 <= row_index < len(rows):
        row = rows[row_index]
        if len(row) >= 5:
            row[4] = '1'
            row[3] = '0'
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(rows)
    button.destroy()
    load.load_grid_from_csv(grid, 'save.csv')
    renderer.render_unit(grid, filename)
    renderer.render_city(grid, filename)    
    gui.baseUI(root, filename)

    print(checkProduhiton(xCell, yCell, filename))

def ProduceUnit(UnitIndex, buttons, grid, filename, root):
    if turn_handler.getMoney(filename):
        if UnitIndex == 0:
            print("Producing settler")   
            production.SpawnUnit(1, filename)
        if UnitIndex == 1:
            print("Producing Melee")
            production.SpawnUnit(2, filename)
        if UnitIndex == 2:
            print("Producing Ranged")
            production.SpawnUnit(3, filename)        
        for button in buttons:
            button.destroy()
        renderer.render_unit(grid, filename)
        renderer.render_city(grid, filename)

        gui.baseUI(root, filename)

    else:
        print("No mone")
def checkProduhiton(x, y, filename):
    production = 0
    adjacentEven_coords = [(x-1, y), (x+1, y), (x, y-1), (x, y+1), (x-1, y+1), (x-1, y-1)]
    adjacentOdd_coords = [(x-1, y), (x+1, y), (x, y-1), (x, y+1), (x+1, y+1), (x+1, y-1)]

    rows = getRowsFromCsv(filename)

    adjacent_coords = adjacentEven_coords if y % 2 == 0 else adjacentOdd_coords

    for adj_x, adj_y in adjacent_coords:
        adj_row_index = adj_y * 50 + adj_x
        if 0 <= adj_row_index < len(rows):
            adj_row = rows[adj_row_index]
            if int(adj_row[2]) == 2:
                production += 1
            if int(adj_row[2]) == 3:
                production += 2
            if int(adj_row[4]) > 0:
                production += -1
    # Write production value to index [2] in row 1251
    if len(rows) >= 1251:  # Ensure the file has at least 1251 rows
        rows[1250][2] = str(production)

    # Write the modified data back to the CSV file
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(rows)
    return production


