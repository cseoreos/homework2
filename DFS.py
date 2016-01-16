from checkGoal import check_if_goal

def depth_first_search():
	while frontier:
		node = frontier.pop()
		if (check_if_goal(node)):
			return node
		if [node[0], node[1], node[2]] in visited: continue
		visited.append([node[0], node[1], node[2]])
		childbranch = getchildren(node)
		for child in childbranch:
			if [child[0], child[1], child[2]] in visited: continue
			frontier.append(child)
			
def getchildren(node):
	children = []
	#sucking
	if(node[2] == 0 and node[0] != 0):
		children.append((0, node[1], node[2], node[3]+"S"))
	elif(node[2] == 1 and node[1] != 0):
		children.append((node[0], 0, node[2], node[3]+"S"))

	#Right
	if(node[2] == 0):
		children.append((node[0], node[1], 1, node[3]+"R"))

	#Left
	if(node[2] ==1):
		children.append((node[0], node[1], 0, node[3]+"L"))

	return children

vac = raw_input("Enter: ")
nums = vac.split(", ")
for k in range(len(nums)):
	nums[k] = int(nums[k])
nums.append("")
frontier = []
visited = []
frontier.append(nums)
if(check_if_goal(nums) == True):
	print ""
	quit()
elif(check_if_goal(nums) ==  "invalid input"):
	print "invalid input"
	quit()
final = depth_first_search()
print final[3]