## 添加java环境
from os import environ
# environ['JAVA_HOME']='D:\Java\java8'
# environ['PYSPARK_HOME']='C:/Users/刘楷/AppData/Local/Programs/Python/Python311/python.exe'
# environ['HADOOP_HOME']='D:/Hadoop/hadoop-3.0.0.tar/hadoop-3.0.0'

from pyspark import SparkConf,SparkContext

## 创建执行环境入口对象
conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")
conf.set("spark.default.parallelism","1")
sc = SparkContext(conf=conf)
print(sc.version)

## 需求1：

Rdd1 = sc.textFile("D:/Python学习/pyspark/search_log.txt")
## print(Rdd1.collect())
#Rdd2 = Rdd1.flatMap(lambda x:x.split("\t")).map(lambda y:y[0][:2])
Rdd2 = Rdd1.map(lambda x:x.split("\t")).map(lambda y:((y[0][:2]),1)).reduceByKey(lambda x,y:x+y).sortBy(lambda x:x[1] ,ascending = False ,numPartitions = 1)
print(Rdd2.collect())
num1 = Rdd2.take(3)
## print(num1)
print(f"热门搜索时间段前三分别是：\n{num1[0]}\n{num1[1]}\n{num1[2]}\n")
print("--------------------")
## 需求2：

Rdd3 = Rdd1.map(lambda x:x.split("\t")).map(lambda y:(y[2],1)).reduceByKey(lambda x,y:x+y).sortBy(lambda x:x[1] ,ascending = False ,numPartitions = 1)
print(Rdd3.collect())
num2 = Rdd3.take(3)
print(f"热门搜索词前三分别是：\n{num2[0]}\n{num2[1]}\n{num2[2]}\n")
print("--------------------")
## 需求3：

Rdd4 = Rdd1.map(lambda x:x.split("\t")).filter(lambda x : True if x[2] == "黑马程序员" else False).map(lambda y:((y[0][:2]),1)).reduceByKey(lambda x,y:x+y).sortBy(lambda x:x[1] ,ascending = False ,numPartitions = 1)
print(Rdd4.collect())
num3 = Rdd4.take(1)
print(f"热门搜索词'黑马程序员'搜索时段最多是：\n{num3[0]}")
print("--------------------")
## 需求4：

Rdd5 = Rdd1.map(lambda x:x.split("\t")).map(lambda y:{"time":y[0],"user_id":y[1],"key_word":y[2],"rank1":y[3],"rank2":y[4],"url":y[5]})
Rdd5.saveAsTextFile("D:/Python学习/pyspark/搜索引擎日志")
## 切记需修改RDD分区为1


sc.stop()



