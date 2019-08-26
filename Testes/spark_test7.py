#file_name = r"C:\Users\jmorais\semantix\spark_files\access_log_Jul95_litle"
file_name = r"C:\Users\jmorais\semantix\spark_files\access_log_Aug95_litle"

ip_counts = {}
list = []
with open(file_name) as logfile:
    _ = logfile.readlines()
    for line in _:	
        try: 
			ip_counts[line.split()[0]] += 1
        except Exception:
            ip_counts[line.split()[0]] = 1

for ip in sorted(ip_counts, reverse=True):
	list = (ip, ip_counts[ip])

for it in sorted(list, reverse=True):
	print "%s %s" % (it, ip_counts[it])
