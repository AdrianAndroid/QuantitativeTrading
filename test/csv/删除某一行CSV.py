import csv

# 定义要删除的行的索引（从0开始）
row_index_to_delete = 2  

# 存储所有行的列表
new_rows = []

# 读取CSV文件
with open('sh000001-example.csv', 'r', encoding='utf-8', newline='') as file:
    reader = csv.reader(file)
    for index, row in enumerate(reader):
        # 如果当前行不是要删除的行，则添加到新行列表中
        if index != row_index_to_delete:
            new_rows.append(row)

print(new_rows)

# 将新行列表写回到CSV文件中
with open('sh000001-example.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(new_rows)