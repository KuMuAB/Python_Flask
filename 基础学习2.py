import collections
from numpy import NaN, index_exp
import pandas as pd
from pandas.core.frame import DataFrame
from pandas.io.formats.style import jinja2
from pandas.io.parsers import count_empty_vals
# from pandas.core.strings import str_strip
# df1 = pd.DataFrame(
#    [ [1,2],
#     [3,4]],
#     columns=['A','B'],
#     index=['X','Y']
# )

# df2 = pd.DataFrame(
#    [ [10,20],
#     [30,40]],
#     columns=['C','B'],
#     index=['Z','Y']
# )


# +
# 这句话生成的是NaN
# df1.add(df2,fill_value=NaN)    
# 这句话生成的是应该的数字
# df1.add(df2,fill_value=0)

# —
# df1.sub(df2,fill_value=0)

# *
# df1.mul(df2,fill_value=0)

# df = pd.read_excel('鹤壁服务站.xlsx',
# sheet_name=3,
# header=[0,1]    #?
# )
# df_total = df['京东'] + df['淘宝']

# df_total.columns = pd.MultiIndex.from_product(    #创建两个表头
#     [
#     ['总计'],
#     df_total.columns
#     ]
# )

# # 行索引进行左右拼接
# df.join(df_total)  





# 字符串

# 去除空白
str1 = ' ajc '
# str1.strip()   #去除两边空白
# str1.lstrip()  #去除左边的空白
# str1.rstrip()  #去除右边的空白


# 拆分成列表  split()
str2 = 'a a a b a c d:e:f:g'
# str2.split()     #按照空格拆分
# str2.split(':')  #按照 : 拆分

# replice  替换
# str2.replace('f','x')

# contains   包含  为true
# str2.__contains__('a')

# count 计数
# str2.count('a')

# index find in  查找
# str2.index('a')    #找的是第一个位置所在下标
# str2.find('a')
# 'a' in str2  

# join  粘合

# ','.join('absd')
# ':'.join(['a','b','c','d'])


# lower  小写   upper  大写
# 'ABcd'.lower()
# 'ABcd'.upper()


# pandas 清洗空值
# df = pd.read_csv('property-data.csv')
# df['NUM_BEDROOMS']              #这是输出具体数值
# is.null()判断各个单元合格是否为空  但是Pandas认为na不是空数据，所以可以指定空数据
# df['NUM_BEDROOMS'].isnull()   #这是输出bool值

'''
DataFrame.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)

axis：默认为 0，表示逢空值剔除整行，如果设置参数 axis＝1 表示逢空值去掉整列。
how：默认为 'any' 如果一行（或一列）里任何一个数据有出现 NA 就去掉整行，如果设置 how='all' 一行（或列）都是 NA 才去掉这整行。
thresh：设置需要多少非空值的数据才可以保留下来的。
subset：设置想要检查的列。如果是多个列，可以使用列名的 list 作为参数。
inplace：如果设置 True，将计算得到的值直接覆盖之前的值并返回 None，修改的是源数据。
'''

# 指定空数据
missing_values = ['n/a','na','--']
df = pd.read_csv('property-data.csv')
df.dropna(inplace=True)
# df['NUM_BEDROOMS'] 
df.to_string()

# 删除包含空数据的行


