import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Month数据类型为str
dates = pd.read_excel('Sales.xlsx',dtype={'Month':str})

# plt.bar(dates.index,dates.Revenue)
plt.title('Sales')   # 标题
slope,intercept,r,p,std_err = linregress(dates.index,dates.Revenue)

exp = dates.index*slope + intercept
plt.scatter(dates.index,dates.Revenue)
plt.plot(dates.index,exp,color='orange')

plt.xticks(dates.index,dates.Month,rotation=90)

# plt.tight_layout()
plt.show()