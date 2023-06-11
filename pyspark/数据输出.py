import os
## os.environ['JAVA_HOME']='D:/Java/java8'
# os.environ['HADOOP_HOME']='D:/Hadoop/hadoop-3.0.0.tar/hadoop-3.0.0/bin'
from pyspark import SparkConf,SparkContext

conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")
sc = SparkContext(conf=conf)

print(sc.version)

## (1):collect()方法的作用是将RDD对象转换为Python对象，返回值是一个list，帮助输出

## (2):reduce()方法的作用是将RDD对象进行聚合，与"数据计算"中的reduceByKey()方法用法相同
rdd1 = sc.parallelize([1,2,3,4,5])
num1 = rdd1.reduce(lambda x,y:x+y)
print(num1)
## 可直接打印reduce()的返回值，返回值等同于计算函数的返回值
## 输出结果为:15

## (3):take(n)方法的作用是将RDD数据集中的数据取出前n个数据，并返回为list
rdd2 = sc.parallelize([1,2,3,4,5])
num2 = rdd2.take(3)
print(num2)
## 输出结果为:[1,2,3]

## (4):count()方法的作用是计算RDD数据集中有多少个数据，返回值是一个数字
rdd3 = sc.parallelize([1,2,3,4,5])
num3 = rdd3.count()

print(num3)
## 输出结果为:5

## (5):saveAsTextfile()方法的作用是将RDD数据集内容写入一个文件
## 调用saveAsTextfile()方法需要配置hadoop环境依赖，还需要修改RDD分区为1，可在用两种方法进行设置
rdd4 = sc.parallelize([1,2,3,4,5],1)
rdd4.saveAsTextFile("D:/Python学习/pyspark/output")

sc.stop()


