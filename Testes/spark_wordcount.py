from pyspark import SparkConf, SparkContext

sc = SparkContext()
textFile = sc.textFile(r"C:\Users\jmorais\spark_in.sql")
wordCounts = textFile.flatMap(lambda line: line.split()).map(lambda word: (word, 1)).reduceByKey(lambda a, b: a+b)
for wc in wordCounts.collect():
 print (wc)