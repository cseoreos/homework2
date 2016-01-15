def check_if_goal(nums):
	if ((int(nums[0]) == 0) and (int(nums[1]) == 0) and (int(nums[2]) < 2)):
		return True
	elif (int(nums[0]) < 0 or int(nums[1]) < 0 or int(nums[2]) < 0):
		return "invalid input"
	elif (int(nums[0]) < 2 and int(nums[1]) < 2 and int(nums[2]) < 2):
		return False
	elif (int(nums[0]) > 1 or int(nums[1]) > 1 or int(nums[2]) > 1):
		return "invalid input" 