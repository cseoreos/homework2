from problem21_3 import getAllChildren
from problem21_1 import *

DEPTH_LIMIT = 5

def depthLimitedSearch(tup_node):
	frontier = []
	frontier.append([tup_node,""])
	seq = ["S","R","L"]
	allNodes = set()

	while len(frontier) != 0:
		node = frontier.pop()
		tnode = node[0]
		
		res = isGoal(tnode,False)
		if res == 1:
			print "".join(node[1])
			break
		elif res == -1:
			break

		if len(node[1]) < DEPTH_LIMIT:
			if tnode not in allNodes:
				allNodes.add(tnode)
				for idx, child in enumerate(reversed(getAllChildren(tnode,allNodes))):
					if child != None and child not in allNodes:
						frontier.append([child, node[1] + seq[idx]])

if __name__ == "__main__":
	for line in stdin:
		try:
			line = re.sub("\s*", "", line)
			if len(line) == 0:
				continue
			val_tup = tuple(map(lambda x: int(x.strip()), line.split(",")))
			depthLimitedSearch(val_tup)
		except:
			print "invalid input"