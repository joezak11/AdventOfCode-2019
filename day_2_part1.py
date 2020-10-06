with open("input_2.txt") as f:
	nums = [int(i) for i in f.read().split(",")]
nums[1] = 12
nums[2] = 2
for i in range(0, len(nums), 4):
	if nums[i] == 1:
		nums[nums[i+3]] = nums[nums[i+1]] + nums[nums[i+2]]
	if nums[i] == 2:
		nums[nums[i+3]] = nums[nums[i+1]] * nums[nums[i+2]]
	if nums[i] == 99:
		break
print(nums[0])