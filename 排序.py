from datetime import date
import pandas as pd


# s1 = pd.Series([1,2,3,4],index = [1,2,3,4],name = 'A')
# s2 = pd.Series([10,20,30],index = [1,2,3],name = 'B')
# s3 = pd.Series([100,200,300],index = [1,2,3],name = 'C')

# # 按照字典的形式插入   内容 行名  列名   内容和行名数量要统一
# df = pd.DataFrame({s1.name:s1,s2.name:s2,s3.name:s3})

# # 按照list的形式插入  内容  列名  行名
# # df = pd.DataFrame([s1,s2,s3])
# print(df)


# dates = pd.read_excel(
#     '鹤服务站.xlsx',  #文件名
#     sheet_name=4,    #表名  
#     skiprows=1,    #跳过空表行
#     usecols='A,B,C,D'   #读取指定列
#     )

# print(dates)



# 排序  和 多重排序

products = pd.read_excel('te2.xlsx',
    sheet_name=2,
    index_col='ID',
    )

# # 从大到小排序      排序方式是ascending
# products.sort_values(
#     by = 'Price',  #by是排序的列名
#     inplace=True,  #inplace是代表当前表格排序
#     ascending=False  #排序方式是ascending
#     )

# # 从小到大
# products.sort_values(
#     by = 'Price',  #by是排序的列名
#     inplace=True,  #inplace是代表当前表格排序
#     ascending=True  #排序方式是ascending
#     )

# 多重排序   将多个列名 组成一个列表
products.sort_values(
    by = ['Worthy','Price'],  #先按照Worthy排  再按照Price排 
    inplace=True,  #inplace是代表当前表格排序
    ascending=[True,False]  #Worthy按照从小到大，Price按照从大到小
    )

print(products)