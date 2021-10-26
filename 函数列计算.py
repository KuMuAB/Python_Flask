import pandas as pd
import numpy as np
from pandas.io import sql

def get_circumcircle_area(l,h):
   r  = np.sqrt(l**2 + h**2) / 2
   return np.pi*r**2

def wrapper(row):
    return get_circumcircle_area(row['Length'],row['Height'])

dates = pd.read_excel('Rectangles.xlsx',index_col='ID')
# dates['CA'] = dates.apply(wrapper,axis=1)


dates['CA'] = dates.apply(lambda  row:get_circumcircle_area(row['Length'],row['Height'])\
,axis=1)


print(dates)

