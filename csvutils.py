import csv 

def getRowsFromCsv(filename):
    with open(filename, 'r', newline='') as csvfile:
        rows = list(csv.reader(csvfile))
        return rows