from datetime import date
import pandas as pd

dates = pd.read_excel(
    'Students.xlsx',
    index_col='ID'
)
# 获取数据
temp = dates[['Test_1','Test_2','Test_3']]
row_sum = temp.sum(axis=1)   # 按照行求和
row_mean = temp.mean(axis=1)  # 平均值
dates['Total'] = row_sum
dates['Average'] = row_mean
col_mean = dates[['Test_1','Test_2','Test_3','Total','Average']].mean()
col_mean['Name'] = 'Summary'

dates = dates.append(col_mean,ignore_index=True)

print(dates)




# print(dates)