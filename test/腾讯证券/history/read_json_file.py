import json

with open('jsons/sh600019.json', 'r', encoding='utf-8') as file:
    json_data = json.load(file)
print(json_data)

data = json_data['data']
history = data['history']
print(type(history), history)
print('|'.join(history))
history.sort()
print(history)

# data2 = json_data['data2']
print('data' in json_data, 'data2' in json_data, 'history' in json_data)