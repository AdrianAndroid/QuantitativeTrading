import pandas as pd

# 要插入的新行数据
new_row = {'Name': 'NewName', 'Age': 28, 'City': 'NewCity'}
# 要插入的位置（从0开始计数）
insert_position = 2

# 读取CSV文件
df = pd.read_csv('input.csv')

# 创建一个新的DataFrame来表示要插入的行
new_df = pd.DataFrame([new_row])

# 将原DataFrame分割成两部分
part1 = df[:insert_position]
part2 = df[insert_position:]

# 拼接三部分DataFrame
result = pd.concat([part1, new_df, part2], ignore_index=True)

# 将修改后的数据保存回CSV文件
result.to_csv('input.csv', index=False)