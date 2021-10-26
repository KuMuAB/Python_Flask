import pandas as pd

dates = pd.read_excel(
    'Students_Duplicates.xlsx',
    # index_col='ID'
)
#    去重
# # 如果根据多列去重，可以给subset一个列表
# # keep=first  表示保存前面的重复值   keep=last  保存后面的重复值
# dates.drop_duplicates(subset='Name',inplace=True,keep='last')


#    找重复
dupe = dates.duplicated(subset='Name')
dupe = dupe[dupe]
print(dupe.index)  
print(dates.iloc[dupe.index])
