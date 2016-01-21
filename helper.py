'''
Gurkirat Singh: A11593827
Anirudh Chava:  A99415981
Jason Geneste:  A11357496
'''

from sys import stdin
from operator import *
import re, heapq

seq = ["L", "U", "R", "D", "S"]
seq_one = ["L", "R", "S"]

def readCallFuncs(func):
	for line in stdin:
		try:
			line = re.sub("\s*", "", line)
			if len(line) == 0:
				continue
			val_tup = tuple(map(lambda x: int(x.strip()), line.split(",")))
			res = func(val_tup)
			if type(res) == str:
				print res
		except:
			print "invalid input"

def readCallFuncsLargeEnv(func):
	dim_lst = []
	for line in stdin:
		try:
			line = re.sub("\s*", "", line)
			if len(line) == 0:
				continue
			state_lst = tuple(map(lambda x: int(x.strip()), line.split(",")))
			dim_lst.append(state_lst)
		except:
			print "invalid input"

	res = func(tuple(dim_lst))
	if type(res) == str:
		print res

def getAllChildren(node,allNodes):
	
	allChildren = [None] * 3
	curr_loc = node[-1]

	#left state
	if curr_loc > 0:
		left_list = list(node)
		left_list[-1] -= 1
		tmp_tup = tuple(left_list)
		if tmp_tup not in allNodes:
			allChildren[0] = tmp_tup

	#right state
	if curr_loc < (len(node[:-1]) - 1):
		right_list = list(node)
		right_list[-1] += 1
		tmp_tup = tuple(right_list)
		if tmp_tup not in allNodes:
			allChildren[1] = tmp_tup

	#suck state
	if node[curr_loc] != 0:
		suck_list = list(node)
		suck_list[curr_loc] = 0
		tmp_tup = tuple(suck_list)
		if tmp_tup not in allNodes:
			allChildren[2] = tmp_tup
			
	return allChildren

def getAllChildrenLargeEvn(node, allNodes):
	
	#list of tuples
	allChildren = [None] * 5
	curr_loc_lst = node[-1]
	curr_row = curr_loc_lst[0]
	curr_col = curr_loc_lst[1]
	row_size = len(node) - 1
	col_size = len(node[0])
	suck_loc = node[curr_row][curr_col]
	op_dict = {
		"L" : [curr_col, gt, 0, sub],
		"R" : [curr_col, lt, col_size - 1, add],
		"U" : [curr_row, gt, 0, sub],
		"D" : [curr_row, lt, row_size - 1, add],
		"S" : [suck_loc, ne, 0, sub]
	}

	
	for idx, val in enumerate(seq):
		
		op_list = op_dict[val]
		if op_list[1](op_list[0],op_list[2]):

			tmp_loc_list = ()
			child = list(node)
			updated_row_col = op_list[3](op_list[0], 1)

			if val != "S":
				if val == "L" or val == "R":
					tmp_loc_list = (curr_row, updated_row_col)
				else:
					tmp_loc_list = (updated_row_col, curr_col)
				child[-1] = tmp_loc_list
				
			else:
				#sucking
				tmp_list = list(child[curr_row])
				tmp_list[curr_col] = updated_row_col
				child[curr_row] = tuple(tmp_list)

			child = tuple(child)
			if child not in allNodes:
				allChildren[idx] = child
	
	return allChildren

class PriorityQueue:
	def __init__(self):
		self._qu = []
		self._idx = 0

	def push(self, data):
		heapq.heappush(self._qu, (data[0], self._idx, data))
		self._idx += 1

	def pop(self):
		return heapq.heappop(self._qu)

	def empty(self):
		return not len(self._qu)
