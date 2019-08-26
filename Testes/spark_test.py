visitors = dict()
# this should be same for each line
line = '95.11.113.x - [15/Nov/2013]'
ip = line.split(" - ")[0]  # assuming it must have " - " in line
visitors[ip] = line

# finally when you are done with above things
for visitor in visitors:
    print visitors[visitor]
	
