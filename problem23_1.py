from helper import *

def isGoal(dim_lst, toPrint=True):

	row_size = (len(dim_lst) - 1)
	col_size = len(dim_lst[0])
	matrix_size =  row_size * col_size
	loc = dim_lst[-1]
	is_bad = 0
	loc_is_bad = 0

	for idx in dim_lst[:-1]:
		is_bad |= reduce(lambda i,j: i|j, idx)
	
	if loc[0] >= row_size or loc[1] >= col_size or loc[0] < 0 or loc[1] < 0:
		loc_is_bad = 1
	
	if is_bad < 0 or is_bad > 1 or loc_is_bad:
		print "invalid input"
		return -1
	elif is_bad == 1:
		if toPrint:
			print "False"
		else:
			return 0
	else:
		if toPrint:
			print "True"
		else:
			return 1

if __name__ == "__main__":
	readCallFuncsLargeEnv(isGoal)