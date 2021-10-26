import pandas as pd

dates = pd.read_excel('Students.xlsx',index_col='ID')
print(dates)