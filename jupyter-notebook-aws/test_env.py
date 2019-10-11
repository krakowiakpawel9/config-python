import findspark
findspark.init('/home/ubuntu/spark-2.4.4-bin-hadoop2.7')

from pyspark import SparkConf, SparkContext

sc = SparkContext(conf=SparkConf())
lines = sc.textFile('/home/ubuntu/config-python/jupyter-notebook-aws/test.txt')
rdd = lines.map(lambda line: line.split())
print(rdd.collect())

