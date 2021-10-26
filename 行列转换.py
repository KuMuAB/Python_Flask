import pandas as pd

# 解决行显示不完的问题
pd.options.display.max_columns=999    
dates = pd.read_excel(
    'Videos.xlsx',
    index_col='Month'
)
table = dates.transpose()


print(table)