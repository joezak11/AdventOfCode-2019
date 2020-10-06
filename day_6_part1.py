class Planet:
	def __init__(self, value):
		self.value = value
		self.parent = set()
		self.children = set()

def parser(data):
	info = {}
	for i in data:
		i = i.split(")")
		if i[0] not in info:
			info[i[0]] = Planet(i[0])
		if i[1] not in info:
			info[i[1]] = Planet(i[1])
		info[i[0]].children.add(info[i[1]])
		info[i[1]].parent.add(info[i[0]])
	return set(info.values())

def search(children, counter):
	for x in children:
		counter += len(x.children)
		counter = search(x.children, counter)
	return counter

with open("input_6.txt") as file:
	data = file.read().splitlines()
data = parser(data)
counter = 0
for i in data:
	counter += len(i.children)
	counter = search(i.children, counter)
print(counter)