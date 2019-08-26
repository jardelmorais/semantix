visitors = dict()

with open(r"C:\Users\jmorais\semantix\spark_files\access_log_Jul95_litle") as fp:
    for line in fp:        
		line = line.split(' - ')[0]  # assuming it must have " - " in line
		ip = line.split(' - ')[0]  
		visitors[ip] = line

for ips in visitors:
   print visitors[ips]

	
#od[name]["Count"] += 1