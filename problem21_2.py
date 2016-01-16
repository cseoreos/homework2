from problem21_1 import *
from problem21_3 import getAllChildren
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
			print "".join(node[1])
			break
		elif res == -1:
			break
			
		if tnode not in allNodes:
			allNodes.add(tnode)
			for idx, child in enumerate(getAllChildren(tnode,allNodes)):
				if child != None and child not in allNodes:
					queue.put([child, node[1] + seq[idx]])

if __name__ == "__main__":
	for line in stdin:
		try:
			line = re.sub("\s*", "", line)
			if len(line) == 0:
				continue
			val_tup = tuple(map(lambda x: int(x.strip()), line.split(",")))
			breadthFirstSearch(val_tup)
		except:
			print "invalid input"