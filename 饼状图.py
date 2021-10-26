from numpy import true_divide
import pandas as pd
import matplotlib.pyplot as plt


dates = pd.read_excel(
    'te2.xlsx',
    sheet_name=2,
    index_col='ID',
    )

dates.sort_values(by='Age',inplace=True,ascending = False,
    
    )

#访问这一页
dates.Age.plot.pie( fontsize = 11)
plt.title('Inter',fontsize = 16,fontweight = 'bold')

plt.ylabel('Age',fontsize=12,fontweight=14)
plt.show()
