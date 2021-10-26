import pandas as pd


pd.options.display.max_columns=999   
orders = pd.read_excel(
    'Orders.xlsx'
)

# 这是新列  年份
# orders['Years'] = pd.DatetimeIndex(orders['Date']).year
# 上下两行效果一样
orders['Years'] = pd.DatetimeIndex(orders.Date).year

# groupby方法   通过这两个进行分组
groups = orders.groupby(['Category','Years'])
s = groups['Total'].sum()    #卖的钱数
c= groups['ID'].count()   #卖的件数

pt2 = pd.DataFrame({'Sum':s,'Count':c})
print(pt2)


