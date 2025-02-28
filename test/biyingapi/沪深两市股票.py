from urllib import request
from urllib import parse
import json
import csv
import os
from pathlib import Path

resp = request.urlopen("http://api.biyingapi.com/hslt/list/sdfg56655ertghdsf36")
data = resp.read()
decode_data = data.decode('utf-8')
json_data = json.loads(decode_data)
print(json_data)

# file_path = __file__
# file_name = os.path.basename(file_path)
file_path = Path(__file__)
file_name = file_path.name
csv_file = file_name + '.csv'
print("csv_file:", csv_file)

with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['dm', 'mc', 'jys'])
    for item in json_data:
        writer.writerow([item['dm'], item['mc'], item['jys']])

