from datetime import date
import pandas as pd

def low_score_red(s):    #  不及格的
    color = 'red' if s < 60 else 'black'
    return f'color: {color}'

def hightscores_green(col):    # 每一列最高分
    return ['background-color:lime' if s==col.max() else 'background-solor:white' 
    for s in col]

dates = pd.read_excel('Students.xlsx')

dates.style.applymap(low_score_red,subset=['Test_1','Test_2','Test_3'])\
.apply(hightscores_green,subset=['Test_1','Test_2','Test_3'])

# dates.style.bar('Test_1',vmin = 0)