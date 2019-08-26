from pyspark import SparkConf, SparkContext
from operator import add
import os
from pympler import asizeof
from pyspark.sql.functions import desc

sc = SparkContext()
julyFile = sc.textFile(r"C:\Users\jmorais\semantix\spark_files\access_log_Jul95_litle")
#julyFile = sc.textFile(r"C:\Users\jmorais\semantix\spark_files\access_log_Jul95")
julyFile = julyFile.cache()
augustFile = sc.textFile(r"C:\Users\jmorais\semantix\spark_files\access_log_Aug95_litle")
#augustFile = sc.textFile(r"C:\Users\jmorais\semantix\spark_files\access_log_Aug95")
augustFile = augustFile.cache()

# ----------------------------------------------------------------------------------------
# 1. Numero de hosts unicos.
julyFile_count = julyFile.map(lambda line: line.split()[0]).distinct().count()
augustFile_count = augustFile.map(lambda line: line.split()[0]).distinct().count()
print('Distinct hosts on July: %s' % julyFile_count)
print('Distinct hosts on August: %s' % augustFile_count)

# ----------------------------------------------------------------------------------------
# 2. O total de erros 404.
try:            
	count_404_july = julyFile.filter(lambda line: line.split()[8] == '404').count()
except Exception:
	count_404_july = 0

try:            
	count_404_august = augustFile.filter(lambda line: line.split()[8] == '404').count()
except Exception:
	count_404_august = 0

print('Quantity of Error 404 on July: %s' % count_404_july)
print('Quantity of Error 404 on August: %s' % count_404_august)

# ----------------------------------------------------------------------------------------
# 3. Os 5 URLs que mais causaram erro 404.
#url = julyFile.(group_by_dataframe.count().filter("`count` >= 2").sort(desc("count"))
#for p in url:
	#print(url)

# ----------------------------------------------------------------------------------------
# 4. Quantidade de erros 404 por dia.


# ----------------------------------------------------------------------------------------
# 5. O total de bytes retornados.
rddSize = ((asizeof.asizeof(julyFile))+(asizeof.asizeof(augustFile))/1024)
print('Get Size in KBytes: %s' % rddSize)
