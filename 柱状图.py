from numpy import true_divide
import pandas as pd
import matplotlib.pyplot as plt


dates = pd.read_excel(
    'te2.xlsx',
    sheet_name=2,
    index_col='ID',
    )

dates.sort_values(by='Price',inplace=True,ascending=False)


dates.plot.bar(x='Name',y='Price',title='International Price')
# plt.bar(dates.Name,dates.Price)
plt.tight_layout()
plt.show()



