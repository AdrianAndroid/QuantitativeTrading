import pandas as pd

# 读取CSV文件
df = pd.read_csv('sh000001-example.csv')
# 定义要删除的行的索引（从0开始）
row_index_to_delete = 2
# 删除指定行
df = df.drop(row_index_to_delete)
# 将修改后的数据保存回CSV文件
df.to_csv('input.csv', index=False)