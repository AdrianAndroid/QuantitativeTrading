import pandas as pd

df = pd.read_csv('sh000001-example.csv')
# 定义删除条件，例如删除`Age`列中值大于30的行
condition = df['Age'] > 30
# 删除满足条件的行
df = df[~condition]
# 将修改后的数据保存回CSV文件
df.to_csv('input.csv', index=False)