def process(in_p):
	with open("input_5.txt") as f:
		nums = [int(i) for i in f.read().split(",")]
	nums[nums[1]] = in_p
	i = 2
	while i < len(nums)-1:
		num = str(nums[i]).zfill(5)
		opcode = int(num[3:])
		mode_1 = int(num[2])
		mode_2 = int(num[1])
		if opcode == 1:
			nums[nums[i+3]] = (nums[i+1] if mode_1 else nums[nums[i+1]]) + (nums[i+2] if mode_2 else nums[nums[i+2]])
			i += 4
		elif opcode == 2:
			nums[nums[i+3]] = (nums[i+1] if mode_1 else nums[nums[i+1]]) * (nums[i+2] if mode_2 else nums[nums[i+2]])
			i += 4
		elif opcode == 4:
			result = nums[i+1] if mode_1 else nums[nums[i+1]]
			if nums[i+2] == 99:
				print(result)
				break
			if result:
				break
			i += 2
		elif opcode == 5:
			if (nums[i+1] if mode_1 else nums[nums[i+1]]):
				i = nums[i+2] if mode_2 else nums[nums[i+2]]
			else:
				i += 3
		elif opcode == 6:
			if not (nums[i+1] if mode_1 else nums[nums[i+1]]):
				i = nums[i+2] if mode_2 else nums[nums[i+2]]
			else:
				i += 3
		elif opcode == 7:
			if (nums[i+1] if mode_1 else nums[nums[i+1]]) < (nums[i+2] if mode_2 else nums[nums[i+2]]):
				nums[nums[i+3]] = 1
			else:
				nums[nums[i+3]] = 0
			i += 4
		elif opcode == 8:
			if (nums[i+1] if mode_1 else nums[nums[i+1]]) == (nums[i+2] if mode_2 else nums[nums[i+2]]):
				nums[nums[i+3]] = 1
			else:
				nums[nums[i+3]] = 0
			i += 4
		elif opcode == 99:
			break

process(1)
process(5)