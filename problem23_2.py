from problem23_1 import isGoal
from helper import *
import Queue

def breadthFirstSearch(node_tup):

	queue = Queue.Queue()
	queue.put([node_tup,""])
	seq = ["L", "R", "U", "D", "S"]
	allNodes = set()

	while not queue.empty():
		node = queue.get()
		tnode = node[0]

		res = isGoal(tnode,False)
		if res == 1:
			return "".join(node[1])
		elif res == -1:
			return None
			
		if tnode not in allNodes:
			allNodes.add(tnode)
			for idx, child in enumerate(getAllChildrenLargeEvn(tnode, allNodes, seq)):
				if child != None and child not in allNodes:
					queue.put([child, node[1] + seq[idx]])

	return "None"

if __name__ == "__main__":
	readCallFuncsLargeEnv(breadthFirstSearch)