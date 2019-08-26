from collections import defaultdict
from operator import itemgetter

access = defaultdict(int)
ip_counts = {}

file_name = r"C:\Users\jmorais\semantix\spark_files\access_log_Aug95_litle"

with open(file_name) as f:
  for line in f:
    parts = line.split() # split at whitespace
    access[parts.split(' ')[0] + parts.split(' ')[8]] += 1 # adapt indices here

# print all URLs in descending order
for url, count in sorted(access.iteritems(), key=lambda (_, c): -c):
  print "%d %s" % (count url)