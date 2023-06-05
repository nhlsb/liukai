## 该项目用于将两个不同数据类型的txt文本文件内容读入到数据库中
from pymysql import Connection
from data_define import Record
from file_read import TextFileRead,JsonFileRead
con = Connection(
    host = "localhost",
    port = 3306,
    user= "root",
    password = "123456",
    autocommit = True
    )
print(con.get_server_info())
## 8.0.30

textFileRead = TextFileRead("D:/Python学习/Python使用数据库/2011年1月销售数据.txt")
jsonFileRead = JsonFileRead("D:/Python学习/Python使用数据库/2011年2月销售数据JSON.txt")
list_1 = textFileRead.read_data()
list_2 = jsonFileRead.read_data()
list_3 = list_1+list_2
## print(list_3)

con.select_db("data_read")
cur = con.cursor()  # 创建一个游标对象
for i in list_3:
    sql = f"insert into orders(order_data,order_id,money,province) values('{i.data}','{i.order_id}',{i.money},'{i.province}')"
    ## print(sql)
    cur.execute(sql)    # 使用游标对象添加数据到数据库中

con.close()


