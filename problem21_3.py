from problem21_1 import *

def depthFirstSearch(tup_node):

	#frontier contains [[tuple(), path list]]
	frontier = []
	frontier.append([tup_node,""])
	seq = ["S","R","L"]
	allNodes = set()

	while len(frontier) != 0:
		node = frontier.pop()
		tnode = node[0]
		
		if isGoal(tnode,False):
			print "".join(node[1])
			break

		if tnode not in allNodes:
			allNodes.add(tnode)
			for idx, child in enumerate(reversed(getAllChildren(tnode,allNodes))):
				if child != None and child not in allNodes:
					frontier.append([child, node[1] + seq[idx]])
				

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

if __name__ == "__main__":
	for line in stdin:
		try:
			line = re.sub("\s*", "", line)
			if len(line) == 0:
				continue
			val_tup = tuple(map(lambda x: int(x.strip()), line.split(",")))
			depthFirstSearch(val_tup)
		except:
			print "invalid input"
