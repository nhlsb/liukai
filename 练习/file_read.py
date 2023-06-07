##2构建抽象类，用于读取两个文件
from data_define import Record
import json
class FileRead: ## 顶层设计，即抽象类
    def read_data(self) -> list[Record]:

        pass

class TextFileRead(FileRead):  ##创建子类，继承FileRead类
    def __init__(self,path):   ##设置新参，用于传入文件地址
        self.path = path

    def read_data(self) -> list[Record]:  ## 重写父类方法
        f = open(self.path,"r",encoding="UTF-8")
        record_list = []
        for line in f.readlines():
            line = line.strip()
            data_list = line.split(",")
            ## 取出数据，用于将txt文件中的每行生成一个Record的对象，即record
            record = Record(data_list[0],data_list[1],data_list[2],data_list[3])
            record_list.append(record)
            ##print(record_list)
        f.close()
        return record_list
            
class JsonFileRead(FileRead):  ##创建子类，继承FileRead类
    def __init__(self,path):   ##设置新参，用于传入文件地址
        self.path = path

    def read_data(self) -> list[Record]:
        f = open(self.path,"r",encoding="UTF-8")
        record_list = []
        for line in f.readlines():
            json_dict = json.loads(line)
            record = Record(json_dict["date"],json_dict["order_id"],int(json_dict["money"]),json_dict["province"])
            record_list.append(record)
            ##print(record_list)
        f.close()
        return record_list

if __name__ == '__main__':
    textFileRead = TextFileRead("D:/Python学习/练习/2011年1月销售数据.txt")
    jsonFileRead = JsonFileRead("D:/Python学习/练习/2011年2月销售数据JSON.txt")
    list_1 = textFileRead.read_data()
    list_2 = jsonFileRead.read_data()
    list_3 = list(map(str, textFileRead.read_data()))
    list_4 = list(map(str, jsonFileRead.read_data()))
    ## print(list_1)
    for i in list_1:  ## 对象i在data_define文件中定义过魔术方法__str__,会将内容以str格式输出
        print(i)
    print("..................................")
    for i in list_2:
        print(i)
    
    
