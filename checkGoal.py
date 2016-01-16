'''def check_if_goal(nums):
	if ((int(nums[0]) == 0) and (int(nums[1]) == 0) and (int(nums[2]) < 2)):
		return True
	elif (int(nums[0]) < 0 or int(nums[1]) < 0 or int(nums[2]) < 0):
		return "invalid input"
	elif (int(nums[0]) < 2 and int(nums[1]) < 2 and int(nums[2]) < 2):
		return False
	elif (int(nums[0]) > 1 or int(nums[1]) > 1 or int(nums[2]) > 1):
		return "invalid input" '''

def check_if_goal(nums):
	for i in range(len(nums)-2):
		if((nums[i] < 0) or (nums[i] > 1) or (nums[len(nums)-2] > len(nums)-3) or (nums[len(nums)-2] < 0)):
			return "invalid input"
	for i in range(len(nums)-2):
		if(nums[i] != 0):
			return False
	return True
