'''
Gurkirat Singh: A11593827
Anirudh Chava:  A99415981
Jason Geneste:  A11357496
'''
from problem23_1 import isGoal
from helper import *

def getDirtyNum(dirty_tup):
	ttl_dirty_rooms = 0
	for idx in dirty_tup:
		ttl_dirty_rooms += len(filter(lambda x: x == 1, idx))
	return ttl_dirty_rooms

def ASearch(node_tup):

	queue = PriorityQueue()
	allNodes = set()
	queue.push((getDirtyNum(node_tup[:-1]), node_tup, ""))

	while not queue.empty():
		
		node = queue.pop()
		tnode = node[2][1]

		res = isGoal(tnode, False)
		if res == 1:
			return node[2][2]
		elif res == -1:
			return None

		for idx, child in enumerate(getAllChildrenLargeEvn(tnode, allNodes)):
			if child != None:
				cost = node[0] - getDirtyNum(tnode[:-1])
				final_val = getDirtyNum(child[:-1]) + (cost + 1)
				queue.push((final_val, child, node[2][2] + seq[idx]))
					

	return "None"
	
if __name__ == "__main__":
	readCallFuncsLargeEnv(ASearch)