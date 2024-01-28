import csv
from csvutils import getRowsFromCsv

def get_current_turn(filename):
    
    rows = getRowsFromCsv(filename)
        
    # Ensure there are at least 1251 lines in the file
    while len(rows) < 1251: #laatu
        rows.append([])  # Append empty rows until reaching the desired line
        
    # Extract the current turn number from the 1251st line
    current_turn = int(rows[1250][0]) if rows[1250] else 0  # Assuming the turn number is in the first column
    
    return current_turn

def write_current_turn(filename, current_turn):
    with open(filename, 'r', newline='') as csvfile:
        rows = list(csv.reader(csvfile))

    # Ensure the file has at least 1251 lines
    while len(rows) < 1251:
        rows.append([])  # Append empty rows until reaching the desired line

    # Modify the 1251st line to include the current turn number
    if len(rows[1250]) > 0:
        rows[1250][0] = str(current_turn)  # Update existing turn number
    else:
        rows[1250].append(str(current_turn))  # Add turn number if it doesn't exist

    # Write the modified data back to the CSV file
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(rows)

def endTurn(filename):
    write_current_turn(filename, get_current_turn(filename) + 1)
    print("Turn ended")