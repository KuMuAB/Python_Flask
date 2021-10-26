from numpy import true_divide
import pandas as pd
import matplotlib.pyplot as plt


dates = pd.read_excel(
    'te2.xlsx',
    sheet_name=2,
    index_col='ID',
    )


dates['Total'] = dates.Age + dates.Age2
dates.sort_values(by='Total',inplace=True,ascending=False)
# dates.plot.bar(x='Name',y=['Age','Age2'])    #多条柱状图
dates.plot.bar(x='Name',y=['Age','Age2'],
    stacked = True,
    title = 'Dates Picture',
    
    )   #柱状图叠加  竖着的


# dates.plot.barh(x='Name',y=['Age','Age2'],
#     stacked = True,
#     title = 'Dates Picture',
    
#     )   #柱状图叠加  水平的
plt.xlabel('Name')
plt.ylabel('Age')
plt.show()