from helper import readCallFuncs

def isGoal(val_tup,toPrint=True):
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
	readCallFuncs(isGoal)