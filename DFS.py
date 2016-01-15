from checkGoal import check_if_goal

def depth_first_search():
	while frontier:
		node = frontier.pop()
		if (check_if_goal(node)):
			print "found"
			return node
		if node in visited: continue
		visited.append(node)
		childbranch = getchildren(node)
		#print childbranch
		for child in childbranch:
			if child in visited: continue
			frontier.append(child)
			print child
			'''dictionary[child] = node'''
			
def getchildren(node):
	children = []
	#sucking
	if(node[2] == 0 and node[0] != 0):
		children.append([0, node[1], node[2]])
	elif(node[2] == 1 and node[1] != 0):
		children.append([node[0], 0, node[2]])

	#Left
	if(node[2] ==1):
		children.append([node[0], node[1], 0])

	#Right
	if(node[2] == 0):
		children.append([node[0], node[1], 1])
	return children

vac = raw_input("Enter: ")
nums = vac.split(", ")
frontier = []
#finalnode = []
visited = []
dictionary = {}
frontier.append([int(nums[0]), int(nums[1]), int(nums[2])] )
if(check_if_goal(frontier[0])):
	print ""
	quit()
print depth_first_search()
'''from checkGoal import check_if_goal

def depth_first_search():
	while frontier:
		node = frontier.pop()
		if (check_if_goal(node)):
			finalnode.append(node)
			return True
		if node in visited: continue
		visited.append(node)
		childbranch.append(getchildren(node))
		for child in childbranch:
			if child in visited: continue
			frontier.append(child)
			dictionary[child] = node
	return True

def getchildren(node):
	children = []
	#sucking
	if(node[2] == 0 and node[0] != 0):
		children.append([0, node[1], node[2]])
	elif(node[2] == 1 and node[1] != 0):
		children.append([node[0], 0, node[2]])

	#Left
	if(node[2] ==1):
		children.append([node[0], node[1], 0])

	#Right
	if(node[2] == 0):
		children.append([node[0], node[1], 1])


vac = raw_input("Enter: ")
nums = vac.split(", ")
frontier = []
visited = []
dictionary = {}
finalnode = []
childbranch= []
frontier.append([int(nums[0]), int(nums[1]), int(nums[2])] )

if (depth_first_search() ==  True):
	while (finalnode[0] != None):
		print finalnode[0]
		finalnode[0] = dictionary[finalnode[0]]
else:
	"IM HERE"
'''