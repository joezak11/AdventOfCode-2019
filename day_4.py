def part_1(num, start, end):
	s_num = str(num)
	if len(s_num) != 6:
		return False
	if num < start or num > end:
		return False
	check_double = False
	check_increase = False
	for i in range(len(s_num)-1):
		if s_num[i] == s_num[i+1]:
			check_double = True
		if s_num[i] <= s_num[i+1]:
			check_increase = True
		else:
			check_increase = False
			break
	return check_double and check_increase

def part_2(num, start, end):
	s_num = str(num)
	if part_1(num, start, end):
		for i in s_num:
			if s_num.count(i) == 2:
				return True
	return False

START = 382345
END = 843167

result_1 = 0
result_2 = 0
for i in range(START, END):
	if part_1(i, START, END):
		result_1 += 1
	if part_2(i, START, END):
		result_2 += 1
print(result_1)
print(result_2)