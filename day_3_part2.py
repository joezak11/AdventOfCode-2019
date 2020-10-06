def wire(inst):
	pos = []
	x = 0
	y = 0
	for i in inst:
		direction, steps = i[0], int(i[1:])
		if direction == "U":
			for _ in range(steps):
				x += 1
				pos.append(f"{x}:{y}")
		if direction == "D":
			for _ in range(steps):
				x -= 1
				pos.append(f"{x}:{y}")
		if direction == "R":
			for _ in range(steps):
				y += 1
				pos.append(f"{x}:{y}")
		if direction == "L":
			for _ in range(steps):
				y -= 1
				pos.append(f"{x}:{y}")
	return pos

def common_points(wire_1, wire_2):
	return set(wire_1) & set(wire_2)

with open("input_3.txt") as f:
	inst = f.readlines()
wire_1 = wire(inst[0].split(","))
wire_2 = wire(inst[1].split(","))
cross = common_points(wire_1, wire_2)
for i in cross:
	steps = len(wire_1[:wire_1.index(i)+1]) + len(wire_2[:wire_2.index(i)+1])
	try:
		if result > steps:
			result = steps
	except NameError:
		result = steps
print(result)