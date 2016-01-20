from problem23_1 import isGoal
from helper import *

DEPTH_LIMIT = 7

def depthLimitedSearch(node_tup, dep_limit=DEPTH_LIMIT):

	frontier = []
	frontier.append([node_tup,""])
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
			for idx, child in enumerate(reversed(getAllChildrenLargeEvn(tnode, allNodes))):
				if child != None:
					frontier.append([child, node[1] + seq[-(idx+1)]])

	return "None"

if __name__ == "__main__":
	readCallFuncsLargeEnv(depthLimitedSearch)