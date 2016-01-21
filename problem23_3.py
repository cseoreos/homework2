'''
Gurkirat Singh: A11593827
Anirudh Chava:  A99415981
Jason Geneste:  A11357496
'''
from problem23_1 import isGoal
from helper import *

def depthFirstSearch(node_tup):

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
			
		if tnode not in allNodes:
			allNodes.add(tnode)
			for idx, child in enumerate(reversed(getAllChildrenLargeEvn(tnode, allNodes))):
				if child != None:
					frontier.append([child, node[1] + seq[-(idx+1)]])

	return "None"

if __name__ == "__main__":
	readCallFuncsLargeEnv(depthFirstSearch)