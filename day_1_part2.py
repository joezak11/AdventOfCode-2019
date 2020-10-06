fuel = 0
with open("input_1.txt") as f:
	for i in f.readlines():
		result = (int(i)//3)-2
		while not result <= 0:
			fuel += result
			result = (result//3)-2
print(fuel)