import pandas as pd

df = pd.read_csv('stocks.csv')
for index, row in df.iterrows():
    # for col in df.columns:
    #     print(f"{col}: {row[col]}")
    _code = row[0]
    _name = row[1]
    _type = row[2]
    print(_code, _name, _type)
    break

# for row in df.itertuples():
#     print(f"行索引: {row.Index}")
#     for col in df.columns:
#         print(f"{col}: {getattr(row, col)}")
#     print()


# # 直接遍历索引并打印每一行
# for idx in df.index:
#     print(f"行索引: {idx}")
#     for col in df.columns:
#         print(f"{col}: {df.loc[idx, col]}")
rxz#     print()