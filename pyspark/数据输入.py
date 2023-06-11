## 添加java环境
# from os import environ
# environ['JAVA_HOME']='D:\Java\java8'

from pyspark import SparkConf,SparkContext

## 创建执行环境入口对象
conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")
sc = SparkContext(conf=conf)
print(sc.version)

## 数据输入的本质是得到RDD对象
## (1)将Python中的五种数据容器转换为RDD对象
rdd1 = sc.parallelize([1,2,3,4,5])
rdd2 = sc.parallelize((1,2,3))
rdd3 = sc.parallelize("asdfghjkl")
rdd4 = sc.parallelize({1,2,3,4,5})
rdd5 = sc.parallelize({"key1":"value1","key2":"value2"})

print(rdd1.collect())
print(rdd2.collect())
print(rdd3.collect())
print(rdd4.collect())
print(rdd5.collect())

## (2)将文本文件转换为RDD对象
rdd6 = sc.textFile("D:/Python学习/Python使用数据库/2011年1月销售数据.txt")

print(rdd6.collect())

sc.stop()


