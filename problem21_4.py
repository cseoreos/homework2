from problem21_1 import isGoal
from helper import *

DEPTH_LIMIT = 5

def depthLimitedSearch(tup_node, dep_limit=DEPTH_LIMIT):
	frontier = []
	frontier.append([tup_node,""])
	seq = ["S","R","L"]
	allNodes = set()

	while len(frontier) != 0:
		node = frontier.pop()
		tnode = node[0]
		
		res = isGoal(tnode,False)
		
		if res == 1:
			return "".join(node[1])
		elif res == -1:
			return None

		if len(node[1]) < dep_limit:
			if tnode not in allNodes:
				allNodes.add(tnode)
				for idx, child in enumerate(reversed(getAllChildren(tnode,allNodes))):
					if child != None and child not in allNodes:
						frontier.append([child, node[1] + seq[idx]])

	return "None"

if __name__ == "__main__":
	readCallFuncs(depthLimitedSearch)