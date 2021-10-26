from datetime import date
from numpy import true_divide
import pandas as pd
import matplotlib.pyplot as plt

dates = pd.read_excel(
    'te2.xlsx',
    sheet_name=2,
    index_col='ID',
    )

dates.sort_values(by='Age',inplace=True,ascending = False)
print(dates.corr())    #  各个数据之间的相关性


# 散点图
dates.plot.scatter(x='Name',y='Age')
plt.show()

# 直方图
dates.Name.plot.hist(bins=50)
plt.xticks(fontsize=8)

plt.show()

# 密度图
dates.Name.plot.kde()
plt.show()