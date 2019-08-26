from pyspark import SparkConf, SparkContext

sc = SparkContext()
textFile = sc.textFile(r"C:\Users\jmorais\semantix\spark_files\access_log_Aug95_litle")
wordCounts = textFile.flatMap(lambda line: line.split()).map(lambda word: (word, 1)).reduceByKey(lambda a, b: a+b)
for p in wordCounts.collect():
	print(p)

