import csv
from csvutils import getRowsFromCsv

def get_current_turn(filename):
    rows = getRowsFromCsv(filename)
 
    # Extract the current turn number from the 1251st line
    current_turn = int(rows[1250][0]) if rows[1250] else 0  # Assuming the turn number is in the first column
    
    return current_turn
def get_current_prod(filename):
    rows = getRowsFromCsv(filename)

    # Extract the current turn number from the 1251st line
    current_prod = int(rows[1250][2]) if rows[1250] else 0  # Assuming the turn number is in the third column
    
    return current_prod

def getMoney(filename):#miks tää palauttaa totuusarvon :D
    rows = getRowsFromCsv(filename)
    if int(rows[1250][1]) >= 10:
        rows[1250][1] = str(int(rows[1250][1])-10)
    else:
        return False
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(rows)
    return True #<- this is stupid

def getMoneyActual(filename): #tää on tässä siksi, koska getMoney() on tyhmä
    rows = getRowsFromCsv(filename)
    japs = int(rows[1250][1])
    if type(japs) == None:
        return 0
    else:
        return japs

def write_current_turn(filename, current_turn):
    rows= getRowsFromCsv(filename)

    # Ensure the file has at least 1251 lines
    while len(rows) < 1251:
        rows.append([])  # Append empty rows until reaching the desired line

    # Modify the 1251st line to include the current turn number, Money, and Production
    if len(rows[1250]) > 0:
        rows[1250][0] = str(current_turn)  # Update existing turn number
    else:
        rows[1250].append(str(current_turn))  # Add turn number if it doesn't exist
        rows[1250].extend(['0', '0'])  # Add Money and Production

    # Write the modified data back to the CSV file
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(rows)
def writeMoney(filename, productiom):
    print("Hemuli")
    rows = getRowsFromCsv(filename)
    # Modify the 1251st line to include the current turn number, Money, and Production
    if len(rows[1250]) > 0:
        print("Japs")
        rows[1250][1] = str(productiom + int(rows[1250][1]))  # Update existing turn number    
    # Write the modified data back to the CSV file
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(rows)
def endTurn(filename):
    writeMoney(filename, get_current_prod(filename))
    write_current_turn(filename, get_current_turn(filename) + 1)
    print("Turn ended")