from problem21_1 import isGoal
from helper import *
import Queue

def breadthFirstSearch(tup_node):

	queue = Queue.Queue()
	queue.put([tup_node,""])
	seq = ["L","R","S"]
	allNodes = set()

	while not queue.empty():
		node = queue.get()
		tnode = node[0]

		res = isGoal(tnode,False)
		if res == 1:
			return "".join(node[1])
		elif res == -1:
			break
			
		if tnode not in allNodes:
			allNodes.add(tnode)
			for idx, child in enumerate(getAllChildren(tnode,allNodes)):
				if child != None and child not in allNodes:
					queue.put([child, node[1] + seq[idx]])

	return None

if __name__ == "__main__":
	readCallFuncs(breadthFirstSearch)