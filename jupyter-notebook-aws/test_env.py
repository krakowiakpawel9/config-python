import findspark
findspark.init('/home/ubuntu/spark-2.4.4-bin-hadoop2.7')

from pyspark import SparkConf, SparkContext

sc = SparkContext(conf=SparkConf())
lines = sc.textFile('/home/ubuntu/text.txt')
rdd = lines.map(lambda line: line.split())
print(rdd.collect()
