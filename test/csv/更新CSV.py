import csv

data = []
with open('sh000001-example.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        data.append(row)

print(data)

if len(data) > 1:
    data[1][1] = "new value ..."

with open('sh000001-example.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerows(data)