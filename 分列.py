 import pandas as pd

employees = pd.read_excel(
    'Employees.xlsx',
    index_col='ID'
)

# 如果没有expand = True   则是一列   有的话 就是两列
# 这里的分隔符号是空格  默认是空格   如果有其他分隔符 只需要在split函数中添加即可
df = employees['Full Name'].str.split(expand = True)

employees['First Name'] = df[0]
employees['Last Name'] = df[1]

print(employees)