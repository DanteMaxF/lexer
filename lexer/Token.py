from .Tag import Tag

class Token:

	def __init__(self, tag):
		self.tag = tag
		self.lineNumber = 0
		self.columnNumber = 0

	def toString(self):
		return 'TOKEN - VALUE = ' + str(self.tag)
