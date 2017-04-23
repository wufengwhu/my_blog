__metaclass__=type
class A():
	"""docstring for ClassName"""
	def hello(self):
		print "Hello,  I'm A."

class B(A):
	"""docstring for B"""
	def hello(self):
		print "Hello, I'm B."

class Bird():
	"""docstring for Bird"""
	def __init__(self):
		self.hungry = True
	def eat(self):
		if self.hungry:
			print 'Aaaah...'
			self.hungry = False
		else:
			print 'No, thanks'

			

class SongBird(Bird):
	"""docstring for SongBird"""
	def __init__(self):
		#Bird.__init__(self)
		super(SongBird, self).__init__()
		self.sound = 'Squawk!'

	def sing(self):
		print self.sound

def checkIndex(key):
	pass

		
		
		
		