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

print(dates)

dates.plot(y=['Age','Age2'])
plt.show()