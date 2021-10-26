from datetime import date,datetime


# d是日期  md是有多少月份
def add_month(d,md):  
    yd = md // 12   #这是计算月份中有多少个年
    m = d.month + md % 12   #这是计算剩余的月份
    if m != 12:   #剩余的月份有整年的或者不足一年
        yd += m // 12
        m = m % 12
    return date(d.year + yd,m,d,d.day)

start = date(2013,4,7)
t = add_month(start,3)
print(t)
    