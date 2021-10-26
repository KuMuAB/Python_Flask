from datetime import date
from numpy import true_divide
import pandas as pd
import matplotlib.pyplot as plt
from pandas.core.indexing import IndexSlice


def Score_validation(row):
    if not 0<=row.Score<=100:
        print(f'#{row.ID}\t dates{row.Name} has an invalid score {row.Score}')

dates = pd.read_excel(
    '第一个.xlsx',
    sheet_name=1,
   
)


dates.apply(Score_validation,axis=1)
# dates.Score.apply(lambda x: 0<=x<=100)