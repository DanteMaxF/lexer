from .Tag import Tag

class Token:

	def __init__(self, tag):
		self.tag = tag

	def toString(self):
		return 'TOKEN - VALUE = ' + str(self.tag)
