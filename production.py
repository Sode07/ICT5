import csv

def SpawnUnit(type, filename):
    with open(filename, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        rows = list(csv_reader)
    
    for row in rows:
        print(row)
        if row[0] == '0' and row[2] == '4':
            print("Found:", row)
            row[3] = type
            break
            
    with open(filename, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerows(rows)