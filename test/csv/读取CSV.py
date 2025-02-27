import csv

with open("sh000001.csv", 'r') as file:
    reader = csv.reader(file)
    i = 0
    for row in reader:
        print(i, row)
        i+=1

with open("sh000001.csv", 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        # print(type(row))
        # odict_keys(['Date', 'Open', 'High', 'Low', 'Close', 'Vol'])
        _date = row['Date']
        _open = row['Open']
        _high = row['High']
        _low = row['Low']
        _close = row['Close']
        _vol = row['Vol']
        print(_date, _open, _high, _low, _close, _vol)