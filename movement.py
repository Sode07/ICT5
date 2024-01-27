import csv
import load
import renderer
xOffset = 1.8
yOffset = 1.52
# Global variable to store selected unit position
selected_position = None

def move_unit(event, grid, filename):
    global selected_position

    if selected_position is not None:
        x, y = selected_position
        hexWidth = grid.hexaSize * 3 / xOffset
        hexHeight = grid.hexaSize * yOffset
        xCell = int(event.x / hexWidth)
        yCell = int(event.y / hexHeight)
        # Adjust xCell for every other row
        if yCell % 2 == 1:  # if yCell is odd
            xCell = int((event.x - hexWidth / 2) / hexWidth)

        if (xCell, yCell) in get_adjacent_tiles(x, y):
            print("Moving unit from", x, y, "to", xCell, yCell)
            row_index = y * 50 + x    
            with open(filename, 'r', newline='') as csvfile:
                rows = list(csv.reader(csvfile))
            row_index = y * 50 + x  # Calculate the row index
            if 0 <= row_index < len(rows):
                row = rows[row_index]
                if len(row) == 4:
                    row[3] = '0'  # Set the unit flag to '0' to indicate no unit
            with open(filename, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerows(rows)
            
            row_index = yCell * 50 + xCell    
            with open(filename, 'r', newline='') as csvfile:
                rows = list(csv.reader(csvfile))
            if 0 <= row_index < len(rows):
                row = rows[row_index]
                if len(row) == 4:
                    row[3] = '1'
            with open(filename, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerows(rows)
            load.load_grid_from_csv(grid, 'save.csv')
            renderer.render_unit(grid, filename)
            return
        else:
            print("Invalid move: clicked tile is not adjacent to the selected unit")
    else:
        print("No unit selected")

def select_unit(event, grid, filename):
    global selected_position
    # Get the clicked coordinates
    x = int(event.x / (grid.hexaSize * 3 / xOffset))
    y = int(event.y / (grid.hexaSize * yOffset))

    # Adjust xCell for every other row
    if y % 2 == 1:  # if y is odd
        x = int((event.x - (grid.hexaSize * 3 / xOffset) / 2) / (grid.hexaSize * 3 / xOffset))

    if unit_exists(filename, x, y):
        print("Unit selected at coordinates:", x, y)
        selected_position = (x, y)  # Save selected unit position
    else:
        selected_position = None  # Reset selected unit position if no unit is selected

def is_within_grid_bounds(grid, x, y):
    """Check if the given coordinates are within the grid boundaries."""
    return 0 <= x < grid.width and 0 <= y < grid.height

def get_adjacent_tiles(xCell, yCell):
    """Get the coordinates of adjacent tiles in a hexagonal grid."""
    adjacent_tiles = []
    if yCell % 2 == 0:  # if yCell is even
        adjacent_tiles = [(xCell - 1, yCell), (xCell - 1, yCell - 1), (xCell, yCell - 1),
                          (xCell + 1, yCell - 1), (xCell + 1, yCell), (xCell, yCell + 1)]
    else:  # if yCell is odd
        adjacent_tiles = [(xCell - 1, yCell), (xCell, yCell - 1), (xCell + 1, yCell),
                          (xCell + 1, yCell + 1), (xCell, yCell + 1), (xCell - 1, yCell + 1)]
    return adjacent_tiles

def unit_exists(filename, x, y):
    with open(filename, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if len(row) == 4 and int(row[3]) == 1:
                if int(row[0]) == x and int(row[1]) == y:
                    return True
    return False
