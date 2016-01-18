from problem23_4 import *

ABS_DEPTH_LIMIT = 10

def iterDeepenDFS(tup_node):

	for idx in range(ABS_DEPTH_LIMIT + 1):
		res = depthLimitedSearch(tup_node, idx)
		if res != None and res != "None":
			return res

if __name__ == "__main__":
	readCallFuncsLargeEnv(iterDeepenDFS)