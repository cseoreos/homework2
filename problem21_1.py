from sys import stdin
import re

def isGoal(val_tup,toPrint):
	is_bad = reduce(lambda x,y: x|y, val_tup[:-1])
	
	if is_bad < 0 or is_bad > 1 or val_tup[-1] >= len(val_tup[:-1]) or val_tup[-1] < 0:
		print "invalid input"
		return -1
	elif is_bad == 1:
		if toPrint:
			print "False"
		else:
			return 0
	else:
		if toPrint:
			print "True"
		else:
			return 1

if __name__ == "__main__":
	for line in stdin:
		try:
			line = re.sub("\s*", "", line)
			if len(line) == 0:
				continue
			val_tup = tuple(map(lambda x: int(x.strip()), line.split(",")))
			isGoal(val_tup,True)
		except:
			print "invalid input"