import pandas as pd

page_001 = pd.read_excel('Students_27.xlsx',sheet_name='Page_001',)
page_002 = pd.read_excel('Students_27.xlsx',sheet_name='Page_002',)


# 列的追加，后面的函数作用是删除最后表的列名
Students = page_001.append(page_002).reset_index(drop=True)   

# 列的末尾追加新行
stu= pd.Series({'ID':41,'Name':'Aipy','Score':99})
Students = Students.append(stu,ignore_index=True)

# 更改行中已有数据值
Students.at[39,'Name'] = 'BeiBei'
Students.at[40,'Score'] = 100

# 替换已有行更替数据
stu= pd.Series({'ID':40,'Name':'Tihuan','Score':99})
Students.iloc[39] = stu

# 插入一个新行   切片后组合
stu= pd.Series({'ID':110,'Name':'Qiepian','Score':120})
part1 = Students[:20]
part2 = Students[20:]
Students = part1.append(stu,ignore_index = True)\
.append(part2).reset_index(drop = True)

# 删除数据行 drop()
    # 指定某行
# Students.drop(index = [1,2,3],inplace = True)
    # 利用切片删除中间行
# part3 = Students[:10]
# part4 = Students[14:20]
# Students = part3.append(part4).reset_index(drop = True)


# 按照某个条件删除
    # 这是创造某个条件
for i in range(5,15):
    Students.at[i,'Name'] = ''

# 这是找到符合条件的位置
missing = Students.loc[Students['Name'] == '']
# print(missing)
# print(missing.index)
Students.drop(index = missing.index,inplace = True)

# 获取全新的数据
Students = Students.reset_index(drop = True)

print(Students)


