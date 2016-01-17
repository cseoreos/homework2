from problem23_1 import isGoal
from helper import *

def depthFirstSearch(node_tup):

	frontier = []
	frontier.append([node_tup,""])
	seq = ["S", "D", "R", "U", "L"]
	allNodes = set()

	while len(frontier) != 0:
		node = frontier.pop()
		tnode = node[0]
		print node
		res = isGoal(tnode,False)
		print res
		if res == 1:
			return "".join(node[1])
		elif res == -1:
			return None
			
		if tnode not in allNodes:
			allNodes.add(tnode)
			for idx, child in enumerate(getAllChildrenLargeEvn(tnode, allNodes, seq)):
				if child != None and child not in allNodes:
					frontier.append([child, node[1] + seq[idx]])

	return "None"

if __name__ == "__main__":
	readCallFuncsLargeEnv(depthFirstSearch)