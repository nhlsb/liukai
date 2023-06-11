
## 添加java环境
from os import environ
# environ['JAVA_HOME']='D:/Java/java8'
# environ['PYSPARK_PYTHON']="C:/Users/刘楷/AppData/Local/Programs/Python/Python39/python.exe"

from pyspark import SparkConf,SparkContext

## 创建执行环境入口对象
conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app") ## 链式调用
sc = SparkContext(conf=conf)
print(sc.version)

rdd1 = sc.parallelize([1,2,3,4,5])
print(rdd1.collect())
## (1):通过map()方法处理数据集，如下为乘以10
def fun(data):
    return data * 10
## 等同于lambda x: x*10

## 调用map()方法要求参数必须是函数，且该函数必须是一个既有参数，又有返回值的函数，map()方法的返回值任然是RDD对象，可链式调用
rdd2 = rdd1.map(fun)
## 测试rdd2是否等于[10,20,30,40,50],此处需要添加Python运行环境,但这里因为版本过高所以继续报错,修改需下载3.10版本解释器，忽略
print(rdd2.collect())


## (2):通过flatMap()方法处理数据集，实现将数据集解除嵌套的效果，用法与map()方法相同

## 使用map()方法
## rdd3 = sc.parallelize(["hello world","a good day"])
## rdd4 = rdd3.map(lambda x:x.split(" "))
## print(rdd4.collect())
## 输出结果为:[["hello","world"],["a","good","day"]],未解除嵌套

## 使用flatMap()方法
rdd3 = sc.parallelize(["hello world","a good day"])
rdd4 = rdd3.flatMap(lambda x:x.split(" "))
print(rdd4.collect())
## 输出结果为:["hello","world","a","good","day"]


## (3):通过reduceByKey()方法处理数据集，该方法需要函数作为参数，有分类和聚合的作用，但该方法
## 只针对KV型的RDD数据集生效，即只对二元元组的组合生效，如下所示("男",99)表示一个二元元组

rdd5 = sc.parallelize([("男",99),("男",88),("女",100),("女",90)])
rdd6 = rdd5.reduceByKey(lambda x,y:x+y)
print(rdd6.collect())
## 输出结果为:[("男",187),("女",190)]


## (4):通过filter()方法处理数据集，用于过滤或保留数据，该方法仅需要一个参数，但参数必须是函数，且该函数必须有一个只返回True或False的返回值
## 此处实现过滤出数据集中的偶数
rdd7 = sc.parallelize([1,2,3,4,5])
rdd8 = rdd7.filter(lambda x : True if x%2 == 1 else False)
print(rdd8.collect())
## 输出结果为:[1,3,5]


## (5):通过distinct()方法处理数据集，用于对数据集进行去重，该方法调用无需传参
rdd9 = sc.parallelize([1,1,2,2,3,3,3,4,5,5])
rdd10 = rdd9.distinct()
print(rdd10.collect())
## 输出结果为:[1,2,3,4,5]


## (6):通过sortBy()方法处理数据集，基于你指定的规则对数据集中的数据进行排序,
## 该方法需要三个参数sortBy(func,ascending,numPartitions),分别指(带有排序规则的函数，排序方法，使用分区)
rdd11 = sc.textFile("D:/Python学习/pyspark/hello.txt")
rdd12 = rdd11.flatMap(lambda x:x.split(" ")).map(lambda y:(y,1)).reduceByKey(lambda x,y:x+y)
rdd13 = rdd12.sortBy(lambda x:x[1] ,ascending = False ,numPartitions = 1)
print(rdd13.collect())


## 综合案例1，词频统计
from os import environ
## environ['JAVA_HOME']='D:/Java/java8'
## environ['PYSPARK_HOME']='C:/Users/刘楷/AppData/Local/Programs/Python/Python311/python.exe'

from pyspark import SparkConf,SparkContext

## 创建执行环境入口对象
conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app") ## 链式调用
sc = SparkContext(conf=conf)
print(sc.version)

Rdd1 = sc.textFile("D:/Python学习/pyspark/hello.txt")
print(Rdd1.collect())
Rdd2 = Rdd1.flatMap(lambda x:x.split(" ")).map(lambda y:(y,1))
Rdd3 = Rdd2.reduceByKey(lambda x,y:x+y)
print(Rdd3.collect())

sc.stop()


## 综合案例2，处理城市销售数据
from os import environ
## environ['JAVA_HOME']='D:/Java/java8'
## environ['PYSPARK_HOME']='C:/Users/刘楷/AppData/Local/Programs/Python/Python311/python.exe'

from pyspark import SparkConf,SparkContext
import json

## 创建执行环境入口对象
conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app") ## 链式调用
sc = SparkContext(conf=conf)
print(sc.version)

## 需求1：计算各城市的销售总额，并排序
Rdd1 = sc.textFile("D:/Python学习/pyspark/orders.txt")
Rdd2 = Rdd1.flatMap(lambda x:x.split("|"))
Rdd3 = Rdd2.map(lambda x:json.loads(x)) ## 将JSON文件转换为Python中的字典
Rdd4 = Rdd3.map(lambda y:(y["areaName"],int(y["money"])))
Rdd5 = Rdd4.reduceByKey(lambda x,y:x+y)
Rdd6 = Rdd5.sortBy(lambda x:x[1] ,ascending = False ,numPartitions = 1)
## 此处已完成需求1
print(Rdd6.collect())
print("----------------")
## 需求2：计算所以城市的销售物品类别
Rdd7 = Rdd3.map(lambda y:(y["category"]))
Rdd8 = Rdd7.distinct()
## 此处已完成需求2
print(Rdd8.collect())
print("----------------")
## 需求3：找出北京市的销售物品类别
Rdd9 = Rdd3.filter(lambda x : True if x["areaName"] == "北京" else False)
Rdd10 = Rdd9.map(lambda y:(y["category"])).distinct()
## 此处已完成需求3
print(Rdd10.collect())


sc.stop()


