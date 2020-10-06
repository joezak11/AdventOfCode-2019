with open("input_2.txt") as f:
	orig = [int(i) for i in f.read().split(",")]
nums = orig[:]
for noun in range(0, 99):
	for verb in range(0, 99):
		nums[1] = noun
		nums[2] = verb
		for i in range(0, len(nums), 4):
			if nums[i] == 99:
				break
			if nums[i] == 1:
				nums[nums[i+3]] = nums[nums[i+1]] + nums[nums[i+2]]
			if nums[i] == 2:
				nums[nums[i+3]] = nums[nums[i+1]] * nums[nums[i+2]]
		if nums[0] == 19690720:
			print(100 * noun + verb)
			exit()
		else:
			nums = orig[:]