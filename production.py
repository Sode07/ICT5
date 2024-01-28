import csv

def SpawnUnit(type, filename):
    rows = getRowsFromCsv(filename)
    
    for row in rows:
        print(row)
        if row[0] == '0' and row[2] == '4':
            print("Found:", row)
            row[3] = type
            break
            
    with open(filename, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerows(rows)