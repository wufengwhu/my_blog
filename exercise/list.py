names = [ "Dave", "Mark", "Ann", "Phil" ]
a = names[2]
names[0] = "Jeff"
names.append("Paula")
names.insert(2, "Thomas")
b = names[0:2]
c = names[2:]
d = [1, "Dave", 3.14, ["Mark", 7, 9, [100,101]], 10]
e = [2*s for s in d]
print e

print d[1]
print d[3][2]
print d[3][3][1]
print b
print names