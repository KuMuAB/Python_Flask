from datetime import date
from numpy import true_divide
import pandas as pd
import matplotlib.pyplot as plt

Students = pd.read_excel(
    '鹤壁服务站.xlsx',
    sheet_name='Student',
    index_col='ID'
    )


Scores = pd.read_excel(
    '鹤壁服务站.xlsx',
    sheet_name='Score',
    index_col='ID'
    )

# 两个表格进行合并(merge) on表示根据谁来合并   how表示留存所有数据  .fillna 将NAN变为0
# 默认会找普通列中相同名字的  如果设置index_col='ID' 则必须用on='ID'
table = Students.merge(Scores,how='left',on='ID').fillna(0)
table.Score = table.Score.astype(int)   #  float变为int
print(table)