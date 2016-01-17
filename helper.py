from sys import stdin
import re

def readCallFuncs(func):
	for line in stdin:
		try:
			line = re.sub("\s*", "", line)
			if len(line) == 0:
				continue
			val_tup = tuple(map(lambda x: int(x.strip()), line.split(",")))
			res = func(val_tup)
			if type(res) == str:
				print res
		except:
			print "invalid input"

def getAllChildren(node,allNodes):
	
	allChildren = [None] * 3
	curr_loc = node[-1]

	#left state
	if curr_loc > 0:
		left_list = list(node)
		left_list[-1] -= 1
		tmp_tup = tuple(left_list)
		if tmp_tup not in allNodes:
			allChildren[0] = tmp_tup

	#right state
	if curr_loc < (len(node[:-1]) - 1):
		right_list = list(node)
		right_list[-1] += 1
		tmp_tup = tuple(right_list)
		if tmp_tup not in allNodes:
			allChildren[1] = tmp_tup

	#suck state
	if node[curr_loc] != 0:
		suck_list = list(node)
		suck_list[curr_loc] = 0
		tmp_tup = tuple(suck_list)
		if tmp_tup not in allNodes:
			allChildren[2] = tmp_tup
	
	return allChildren