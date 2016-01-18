from problem23_1 import isGoal
from helper import *
import Queue as Q

def getDirtyNum(dirty_tup):
	ttl_dirty_rooms = 0
	for idx in dirty_tup:
		ttl_dirty_rooms += len(filter(lambda x: x == 1, idx))
	return ttl_dirty_rooms

def ASearch(node_tup):

	queue = Q.PriorityQueue()
	allNodes = set()
	queue.put((getDirtyNum(node_tup[:-1]), node_tup, ""))

	while not queue.empty():
		node = queue.get()
		tnode = node[1]

		res = isGoal(tnode, False)
		if res == 1:
			return "".join(node[2])
		elif res == -1:
			return None

		if tnode not in allNodes:
			allNodes.add(tnode)
			
			for idx, child in enumerate(getAllChildrenLargeEvn(tnode, allNodes)):
				if child != None:
					cost = node[0] - getDirtyNum(tnode[:-1])
					final_val = getDirtyNum(child[:-1]) + (cost + 1)
					queue.put((final_val, child, node[2] + seq[idx]))
					

	return "None"
	
if __name__ == "__main__":
	readCallFuncsLargeEnv(ASearch)