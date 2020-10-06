import itertools

with open("input_7.txt") as f:
	nums = [int(i) for i in f.read().split(",")]
all_seq = itertools.permutations([0, 1, 2, 3, 4])
result = 0
for current_seq in all_seq:
	stdin = 0
	stdin_b = False
	for phase in current_seq:
		i = 0
		temp = nums[:]
		while i < len(temp):
			num = str(temp[i]).zfill(5)
			opcode = int(num[3:])
			mode_1 = int(num[2])
			mode_2 = int(num[1])
			if opcode == 1:
				temp[temp[i+3]] = (temp[i+1] if mode_1 else temp[temp[i+1]]) + (temp[i+2] if mode_2 else temp[temp[i+2]])
				i += 4
			elif opcode == 2:
				temp[temp[i+3]] = (temp[i+1] if mode_1 else temp[temp[i+1]]) * (temp[i+2] if mode_2 else temp[temp[i+2]])
				i += 4
			elif opcode == 3:
				if stdin_b:
					temp[temp[i+1]] = stdin
					stdin_b = False
				else:
					temp[temp[i+1]] = phase
					stdin_b = True
				i += 2
			elif opcode == 4:
				stdin = temp[i+1] if mode_1 else temp[temp[i+1]]
				i += 2
			elif opcode == 5:
				if (temp[i+1] if mode_1 else temp[temp[i+1]]):
					i = temp[i+2] if mode_2 else temp[temp[i+2]]
				else:
					i += 3
			elif opcode == 6:
				if not (temp[i+1] if mode_1 else temp[temp[i+1]]):
					i = temp[i+2] if mode_2 else temp[temp[i+2]]
				else:
					i += 3
			elif opcode == 7:
				if (temp[i+1] if mode_1 else temp[temp[i+1]]) < (temp[i+2] if mode_2 else temp[temp[i+2]]):
					temp[temp[i+3]] = 1
				else:
					temp[temp[i+3]] = 0
				i += 4
			elif opcode == 8:
				if (temp[i+1] if mode_1 else temp[temp[i+1]]) == (temp[i+2] if mode_2 else temp[temp[i+2]]):
					temp[temp[i+3]] = 1
				else:
					temp[temp[i+3]] = 0
				i += 4
			elif opcode == 99:
				break
			else:
				print(f"Unknown: Position: {i} Value: {temp[i]}")
				break
	if stdin > result:
		result = stdin
print(result)