import pandas as pd
from pandas.core.indexes.base import Index


# list_2d = [[1,2],[3,4]]  #这是一个列表
# df = pd.DataFrame(list_2d,  #这是核心数据
# columns=['a','b'],#这是列索引
# index=['x','y']) #这是行索引
# # print(df)
# df

# d = {'A':[1,3],'B':[2,4]}
# df = pd.DataFrame(d,index=['x','y'])
# df 

# 读取excel表
# df = pd.read_excel('鹤壁服务站.xlsx')
# df

# sheet_name  参数
'''

# 读取excel表中的字表  使用sheet_name=int  0 代表第一个字表  以此类推

# # 方法1
# pd.read_excel('鹤壁服务站.xlsx',
# sheet_name=2)

# # 方法2
# pd.read_excel('鹤壁服务站.xlsx',
# sheet_name='第三个')

# 取多个子表中的特定子表
df_dict = pd.read_excel('鹤壁服务站.xlsx',
sheet_name=None)    #生成有个字典反馈
df_dict['第一个']   # 取出多个子表中的对应子表

'''

# header 参数
# header 指定列索引的行
# index_col 指定行索引的列

# pd.read_excel('鹤壁服务站.xlsx',
# sheet_name=1,
# header=1,
# index_col=1)


'''
# usecols:指定某些列   默认是全部列

pd.read_excel('鹤壁服务站.xlsx',
sheet_name=1,
# usecols='B:E', #这样读出来，行标志就没有了
# usecols=['B','E'],    # 提倡使用这种办法  读列名
# usecols=lambda x: x == '第一列',   #可以传入一个函数
# usecols=lambda x: (x=='第一列')|(x == '第三列')   #这个可以单独选取指定列

# skiprows参数   跳过行  skiplows = 1   跳过第1行  注意这里没有跳过列的函数  应为已经有了
# usecols这个函数，所以这两个函数可以搭配使用
# skiprows=1   #这是跳过第一行
# skiprows=[1,3]   #也可以跳过一个列表
# skiprows=2
# names=[' ','第一列', '第二列', '第三列', '第四列', '第五列', '第六列'],
# header=None,  #  如果没有这句，会覆盖掉原来的第一行，导致数据出错
# na_values={'第一列':[11,10,3],'第二列':[4,7,15]}   #这是传入一个字典，可以修改对应列找中的value值数据
# na_values=['a','c']   #这里会把表格中的对应数据变为NaN

# sheet_name = 3,
# converters={   #这个参数可以传递函数，对列数据进行函数化处理
#     # 'a':lambda x: x+2,
#     # 'b':lambda x: x*2,

#     # 0和1分别代表第一列和第二列
#     0:lambda x:x+2,
#     1:lambda x:x*2
# }

# true_values   对字符串有效，整型无效
# false_values
true_values=['A','a'],   #这里列3之所以没转化，是因为整列不能都转化，所以不转化
false_values=['C'],
dtype={'第五列':bool}  #第五列转换成bool型，非0为true  0为false
)
'''

'''
# to_excel() 输出Excel表格

df = pd.DataFrame({
    '销量':[20,30,34],
    '售价':[100,200,300],
},
index=['aaa','bbb','ccc'],  #  这里个数也要一一对应，否则会出错
)   
df.index.name = '货号'    # 如果没有这一句，第一列的列标题是空的，所以这是给列标题起名字

df.to_excel('第一个.xlsx',  #这是一个路径，可以自己选择的生成的位置，也可以就在这个文件夹下
sheet_name = "te1",  # 这是给子表命名字
float_format='%.2f',
)

'''

'''
# ExcelWriter  运用
# 设置datatime输出格式，输出多个sheet


from  datetime import datetime

df1 = pd.DataFrame(
    {'日期':[datetime(2021,2,3),datetime(2021,4,3)],
    '销量':[100,200]
    }
)

df2 = pd.DataFrame(
    {'日期':[datetime(2021,3,3),datetime(2021,5,3)],
    '销量':[1002,2020]
    }
)

with pd.ExcelWriter('te2.xlsx',datetime_format="YYYY-MM-DD") as writer:
    df1.index.name = '月份'
    df1.to_excel(writer,sheet_name='1月')
    df2.index.name = '月份'
    df2.to_excel(writer,sheet_name='2月')
'''

'''
# DataFrame.to_csv   .csv文件的读和写
# 路径，分隔符和编码格式
df = pd.DataFrame(
    {
        'A':[1,2],
        'B':[3,4],
    }
)

df.to_csv('tb1.csv',index=False)

pd.read_csv('tb1.csv')
'''


# index   索引
'''
索引避免重复值
避免使用默认的整数
'''




# df = pd.DataFrame(
#     {
#         'A':[1,4,7],
#         'B':[2,5,8],
#         'C':[3,6,9],
#     },
#     index=list('XYZ')   #这个可以搞行名称
# )
# df

# df[['A']]    #输出A这一列
# df[df['B']>2]   #类似表格中的筛选
# df[0:2]    #这个切片只能切行  0:2  只包括0、1
# df['X':'Y']



# s = pd.Series(
#     {'A':1,'B':2,'C':3
#     }
# )
# s['C']    #  输出3
# s[0:2]
# s[0:-1]
# s[::-1]
# s['A':'B']



'''
# 选择数据
# 行和列选择一个数据    row_indexer   column_indexer

df = pd.DataFrame(
    [[1,2,3,4],[5,6,7,8],[9,10,11,12]],
    columns=list('ABCD'),
    index=list('XYZ')
)
df

# 第一个参数是行索引  第二个是列索引  而且是从0开始的
df.iloc[0,3]

# 切片也可以是参数   但是不包括最后一个数字代表的行和列
df.iloc[1:2,1:3]




# df.loc['X','B']


# 这句代码的意思是  选择X 和 Z行   B 和 D列进行数据的筛选
# df.loc[['X','Z'],['B','D']]

# 这句代码的意思是选择所有的行，B到D列
# df.loc[:,'B':'D']

#  这句代码的意思是   所有行  列倒序
# df.loc[:,::-1]

#  这句代码的意思是   所有列  行倒序
# df.loc[::-1,:]
'''

# 数据赋值

# s = pd.Series({
#     'A':1,'B':2,'C':3
# })
# s
# s[2] = 10
# s.iloc[1] = 20
# s.loc['A'] = 30
# s.loc['D'] = 40
# s.iloc[1:3] = 99

# s[s>50] = 100
# s

# 这句话的意思就是选择的E列中>10的赋值为200
# df.loc[df['E']>10,'E'] = 200


# 加减乘除  需要考虑空值和除数为0的情况



