from numpy import column_stack
import pandas as pd
import numpy as np

page_001 = pd.read_excel('Students_27.xlsx',sheet_name='Page_001',)
page_002 = pd.read_excel('Students_27.xlsx',sheet_name='Page_002',)

students= pd.concat([page_001,page_002]).reset_index(drop=True)

# 追加一列
students['Age'] = 30

# 删除列
students.drop(columns = ['Age','Score'],inplace=True)

# 插入列
students.insert(1,column = 'Foo',value=np.repeat('foo',len(students)))

# 修改列名
students.rename(columns={'Foo':'FOO','Name':'NAME'},inplace=True)


print(students)
