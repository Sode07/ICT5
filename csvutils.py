import csv 

counter = 0
def getRowsFromCsv(filename):
    global counter
    counter = counter + 1  
    print("csv : ", counter)
    with open(filename, 'r', newline='') as csvfile:
        rows = list(csv.reader(csvfile))
        return rows