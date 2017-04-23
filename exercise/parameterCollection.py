
def init(data):
	data['first'] = {}
	data['middle'] = {}
	data['last'] = {}

def lookup(data, label, name):
	return data[label].get(name)

def store(data, *full_names):
	for full_name in full_names:
		print full_name
		names = full_name.split()
		print names
		print len(names)
		if len(names) == 2:
			names.insert(1, '')
			print names
		labels = 'first', 'middle', 'last'
		for label, name in zip(labels, names):
			people = lookup(data, label, name)
			if people:
				people.append(full_name)
			else:
				data[label][name]=[full_name]