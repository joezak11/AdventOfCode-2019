class Planet:
	def __init__(self, value):
		self.value = value
		self.parent = set()
		self.children = set()

def parser(data):
	info = {}
	for i in data:
		i = i[:-1].split(")")
		if i[0] not in info:
			info[i[0]] = Planet(i[0])
		if i[1] not in info:
			info[i[1]] = Planet(i[1])
		if i[1] == "YOU":
			YOU = info[i[0]]
		if i[1] == "SAN":
			SAN = info[i[0]]
		info[i[0]].children.add(info[i[1]])
		info[i[1]].parent.add(info[i[0]])
	return (set(info.values()), YOU, SAN)

def search(data, YOU, SAN, last_step=set(), blacklist=set(), counter=1):
	blacklist |= last_step
	while True:
		next_step = set()
		for i in last_step:
			if SAN in i.children:
				break
			next_step |= (i.parent | i.children) - blacklist
		else:
			last_step = next_step
			blacklist |= next_step
			counter += 1
			continue
		break
	return counter

def dead_end(data):
	blacklist = set()
	for i in data:
		if not i.parent:
			blacklist.add(i)
		for x in i.children:
			if not x.children:
				blacklist.add(x)
	return blacklist

with open("input_6.txt") as file:
	data, YOU, SAN = parser(file)
print(search(data, YOU, SAN, last_step={YOU}, blacklist=dead_end(data)))