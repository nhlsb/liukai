## 该文件用于实现将数据库中的数据写入到txt文件中

import datetime
from pymysql import Connection
with open("re_read_data.txt","w") as f:
    con = Connection(
        host = "localhost",
        port = 3306,
        user= "root",
        password = "123456",
        ## autocommit = True
        )
    ## print(con.get_server_info())
    ## 8.0.30

    con.select_db("data_read")
    cur = con.cursor()  # 创建一个游标对象
    read_sql = f"select * from orders"
    cur.execute(read_sql)    # 使用游标对象执行查询操作
    result = cur.fetchall()  # 使用游标对象读取数据库中的数据
    result_list = list(result)
    ## print(result_list)
    for i in result_list:
         ## print(i[0].strftime('%Y-%m-%d'))
        order_data = list(i)[0].strftime('%Y-%m-%d')
        order_id   = list(i)[1]
        money      = list(i)[2]
        province   = list(i)[3]
        mix = f"{order_data} , {order_id} , {money} , {province}\n"
        ## print(mix)
        f.write(mix)
            
    con.close()

    
    
