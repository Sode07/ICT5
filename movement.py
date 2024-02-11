import csv
import load
import renderer
import gui
import csv_handler
csv_obj = csv_handler.CSV('save.csv')  # Luodaan csv luokka

xOffset = 1.8
yOffset = 1.52
# Global variable to store selected unit position
selected_position = None

def move_unit(event, grid, filename, currentTurn): #TODO korjaa tämä
    global selected_position

    if selected_position is not None:

        x, y = selected_position

        if unit_exists(filename, x, y) == 2: #joutuu lukee csv uudellee vois fiksaa joskus
            print("can't move a city")
            return

        hexWidth = grid.hexaSize * 3 / xOffset
        hexHeight = grid.hexaSize * yOffset
        xCell = int(event.x / hexWidth)
        yCell = int(event.y / hexHeight)
        world = csv_obj.get_array()

        row_index = grid.getIndexFromXY(x, y)  
        if 0 <= row_index < len(world):
            row = world[row_index]
            if int(row[5]) <= currentTurn:
                # Adjust xCell for every other row
                if yCell % 2 == 1:  # if yCell is odd
                    xCell = int((event.x - hexWidth / 2) / hexWidth)

                if (xCell, yCell) in get_adjacent_tiles(x, y):
                    print("Moving unit from", x, y, "to", xCell, yCell) 
                    row_index = grid.getIndexFromXY(x, y) # Calculate the row index
                    if 0 <= row_index < len(world): #en tiiä mitä tää tekee mut en viiti koskee siihe
                        row = world[row_index]
                        if len(row) >= 5:
                            row[3] = '0'  # Set the unit flag to '0' to indicate no unit
                            row[5] = currentTurn
                    
                    row_index = grid.getIndexFromXY(xCell, yCell)

                    if 0 <= row_index < len(world):#tää saattais toimii ilmanki täkä chekkiä. säästettäis pari syklii
                        row = world[row_index]
                        if len(row) >= 5:
                            row[3] = '1'

                    with open(filename, 'w', newline='') as csvfile:
                        writer = csv.writer(csvfile)
                        writer.writerows(world)
                        csv_obj.invalidate_cache()

                    load.load_grid_from_csv(grid, 'save.csv')
                    renderer.render_unit(grid, filename)
                    renderer.render_city(grid, filename)
                    return
                else:
                    print("Invalid move: clicked tile is not adjacent to the selected unit")
    else:
        print("No unit selected")

def select_unit(event, grid, filename, root):
    global selected_position
    # Get the clicked coordinates
    x = int(event.x / (grid.hexaSize * 3 / xOffset))
    y = int(event.y / (grid.hexaSize * yOffset))

    # Adjust xCell for every other row
    if y % 2 == 1:  # if y is odd
        x = int((event.x - (grid.hexaSize * 3 / xOffset) / 2) / (grid.hexaSize * 3 / xOffset))
    if unit_exists(filename, x, y) == 3:
        gui.settlerUI(root, grid, filename, x, y)
    if unit_exists(filename, x, y) >= 1:
        print("Unit selected at coordinates:", x, y)
        selected_position = (x, y)  # Save selected unit position
    if unit_exists(filename, x, y) == 2:
        gui.cityUI(root, grid, filename)

def is_within_grid_bounds(grid, x, y):
    """Check if the given coordinates are within the grid boundaries."""
    return 0 <= x < grid.width and 0 <= y < grid.height

def get_adjacent_tiles(xCell, yCell):
    """Get the coordinates of adjacent tiles in a hexagonal grid."""
    adjacent_tiles = []
    if yCell % 2 == 0:  # if yCell is even
        adjacent_tiles = [(xCell-1, yCell), (xCell+1, yCell), (xCell, yCell-1), (xCell, yCell+1), (xCell-1, yCell+1), (xCell-1, yCell-1)]

    else:  # if yCell is odd
        adjacent_tiles = [(xCell-1, yCell), (xCell+1, yCell), (xCell, yCell-1), (xCell, yCell+1), (xCell+1, yCell+1), (xCell+1, yCell-1)]
    return adjacent_tiles

def unit_exists(filename, x, y):
    reader = csv_obj.get_array()
    for row in reader:
        if len(row) >= 5 and int(row[3]) >= 1:
            if int(row[0]) == x and int(row[1]) == y and int(row[3]) == 1:
                return 3 #???????????????
            elif int(row[0]) == x and int(row[1]) == y:
                return 1 #unit       
        else:
            if int(row[0]) == x and int(row[1]) == y and int(row[4]) > 0:
                return 2 #kaupunki
    return False

def save_last_moved_turn(filename, x, y, turn):
    rows = csv_obj.get_array()

    row_index = y * 50 + x
    if 0 <= row_index < len(rows):
        row = rows[row_index]
        if len(row) >= 6:  # Ensure at least 6 columns are available
            row[5] = turn  # Save the current turn in index 5

    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(rows)
