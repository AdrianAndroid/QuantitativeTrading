import csv

# 要插入的新行数据
new_row = ['NewName', 28, 'NewCity']
# 要插入的位置（从0开始计数）
insert_position = 2

# 存储所有行的列表
all_rows = []

# 读取CSV文件
with open('input.csv', 'r', encoding='utf-8', newline='') as file:
    reader = csv.reader(file)
    for index, row in enumerate(reader):
        print('index=', index, 'row=', row)
        if index == insert_position:
            all_rows.append(new_row)
        all_rows.append(row)

# 如果插入位置是最后一行之后
if insert_position >= len(all_rows):
    all_rows.append(new_row)

# 将所有行写回到CSV文件中
with open('input.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(all_rows)