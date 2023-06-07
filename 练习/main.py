##综合练习
##1数据定义--data_define
##2文件读取--file_read
##3数据绘图--main

from file_read import TextFileRead,JsonFileRead
from data_define import Record
from pyecharts.charts import Bar
from pyecharts.options import *
from pyecharts.globals import ThemeType

textRead = TextFileRead("D:/Python学习/练习/2011年1月销售数据.txt")
jsonRead = JsonFileRead("D:/Python学习/练习/2011年2月销售数据JSON.txt")

list1 = textRead.read_data()
list2 = jsonRead.read_data()
list3 = list1 + list2 ## list3是总的对象列表
##print(list3)
dictall = {}  ## 为了最终创建一个key为data(日期)，value为sum(money)(当前日期下销售额之和)
for i in list3:
    ## print(i)
    if i.data in dictall.keys():    ## i.data 是当前对象的成员变量之一
        dictall[i.data] += i.money  ## i.money是当前对象的成员变量之一
    else:
        dictall[i.data] = i.money
print(dictall)
## print(type(list3[0].money))
## 绘图开始
bar = Bar(init_opts = InitOpts(theme = ThemeType.LIGHT))

bar.add_xaxis(list(dictall.keys()))
bar.add_yaxis("销售额",list(dictall.values()),label_opts = LabelOpts(is_show = False))
bar.set_global_opts(title_opts = TitleOpts())
bar.render("每日销售柱状图.html")


