'''
Gurkirat Singh: A11593827
Anirudh Chava:  A99415981
Jason Geneste:  A11357496
'''
from problem23_1 import *
import Queue

def breadthFirstSearch(node_tup):

	queue = Queue.Queue()
	queue.put([node_tup,""])
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
			for idx, child in enumerate(getAllChildrenLargeEvn(tnode, allNodes)):
				if child != None:
					queue.put([child, node[1] + seq[idx]])

	return "None"

if __name__ == "__main__":
	readCallFuncsLargeEnv(breadthFirstSearch)