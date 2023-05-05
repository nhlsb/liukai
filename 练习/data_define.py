##1数据定义
class Record:
    def __init__(self,data,order_id,money,province):
        self.data = data            ##日期
        self.order_id = order_id    ##编号
        self.money = int(money)     ##金额
        self.province = province    ##省份
    def __str__(self):
        return f"{self.data},{self.order_id},{self.money},{self.province}"
