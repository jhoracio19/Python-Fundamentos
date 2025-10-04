import csv

with open('datos.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Nombre", 'Edad'])
    writer.writerow(["Horacio", '21'])
    writer.writerow(["Naomi", '20'])
    writer.writerow(["Fernanda", '14'])

with open('datos.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)