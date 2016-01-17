from problem21_4 import *

ABS_DEPTH_LIMIT = 8

def iterDeepenDFS(tup_node):

	for idx in range(ABS_DEPTH_LIMIT + 1):
		res = depthLimitedSearch(tup_node, idx)
		if res != None:
			return res

if __name__ == "__main__":
	readCallFuncs(iterDeepenDFS)