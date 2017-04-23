pelple = {
	'Alice':{
		'phone' : '2341',
		'addr' : 'Fool drive 23'
	},

	'Beth' : {
		'phone' : '9102',
		'addr' : 'Bar street 42'
	},

	'Cecil' :{
		'phone' : '3158',
		'addr' : 'Baz avenue 90'
	}
}

labels ={
	'phone' : 'phone number',
	'addr' : 'address'
}

name = raw_input('Name: ')

request = raw_input('phone number(p) or address(a)?')
if request == 'p' : key = 'phone'
if request == 'a' : key = 'addr'

if name in pelple : print "%s's %s is %s." % \
	(name, labels[key], pelple[name][key])

