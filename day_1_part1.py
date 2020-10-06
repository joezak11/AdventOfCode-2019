fuel = 0
with open("input_1.txt") as file:
	for i in file:
		fuel += (int(i)//3)-2
print(fuel)