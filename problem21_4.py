from problem21_1 import isGoal
from helper import *

DEPTH_LIMIT = 5

def depthLimitedSearch(tup_node, dep_limit=DEPTH_LIMIT):
	frontier = []
	frontier.append([tup_node,""])
	allNodes = set()

	while len(frontier) != 0:
		node = frontier.pop()
		tnode = node[0]
		
		res = isGoal(tnode,False)
		
		if res == 1:
			return "".join(node[1])
		elif res == -1:
			return None

		allNodes.add(tnode)
		if len(node[1]) < dep_limit:
			for idx, child in enumerate(reversed(getAllChildren(tnode,allNodes))):
				if child != None:
					frontier.append([child, node[1] + seq_one[-(idx+1)]])

	return "None"

if __name__ == "__main__":
	readCallFuncs(depthLimitedSearch)