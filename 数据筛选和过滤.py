import pandas as pd

#  编写两个函数作为筛选条件
def Age_20_to_60(a):
    return 20<=a<60

def level_a(s):
    return 40<=s<=90


dates = pd.read_excel(
    'te2.xlsx',
    sheet_name=2,
    index_col='ID',
    )

dates = dates.loc[
    # dates['Age'].apply(Age_20_to_60),   #筛选出[20,60)
    # dates.Age.apply(Age_20_to_60),   #和上述效果一样
    dates.Age.apply(lambda x: 20<=x<60)  # 和上述效果一样,lambda 代替函数Age_20_to_60
    ].loc[dates['Price'].apply(level_a)]   #在上述数据中，再次筛选出[40,60]





print(dates)

# 筛选数据