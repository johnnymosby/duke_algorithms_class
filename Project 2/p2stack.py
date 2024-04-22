"""
Math 560
Project 2
Fall 2021

p2stack.py

Partner 1:
Partner 2:
Date:
"""

"""
Stack Class
"""
class Stack:

	"""
	Class attributes:
	stack    # The array for the stack.
	top      # The index of the top of the stack.
	numElems # The number of elements in the stack.
	"""

	"""
	__init__ function to initialize the Stack.
	Note: intially the size of the stack defaults to 3.
	Note: the stack is initally filled with None values.
	Note: since nothing is on the stack, top is -1.
	"""
	def __init__(self, size=3):
		self.stack = [None for x in range(0,size)]
		self.top = -1
		self.numElems = 0
		return

	"""
	__repr__ function to print the stack.
	"""
	def __repr__(self):
		s = '[ ' + ', '.join(map(str, self.stack)) + ' ]\n'
		s += ('Top: %d' % self.top) + '\n'
		s += ('numElems: %d' % self.numElems) + '\n'
		return s

	"""
	isFull function to check if the stack is full.
	"""
	def isFull(self):
		##### IMPLEMENT! #####
		return len(self.stack) == self.numElems

	"""
	isEmpty function to check if the stack is empty.
	"""
	def isEmpty(self):
		##### IMPLEMENT! #####
		return self.numElems == 0

	"""
	resize function to resize the stack by doubling its size.
	"""
	def resize(self):
		##### IMPLEMENT! #####
		self.stack = self.stack + [None for x in self.stack]

	"""
	push function to push a value onto the stack.
	"""
	def push(self, val):
		##### IMPLEMENT! #####
		if self.isFull():
			self.resize()
		self.stack[self.numElems] = val
		self.top = self.numElems
		self.numElems += 1

	"""
	pop function to pop the value off the top of the stack.
	"""
	def pop(self):
		##### IMPLEMENT! #####
		if self.numElems == 0:
			return None
		else:
			value_to_return = self.stack[self.top]
			self.stack[self.top] = None
			self.top -= 1
			self.numElems -= 1
			return value_to_return


def tests():
	s = Stack(3)
	print(s.pop())
	s.push(4)
	s.push(5)
	s.push(6)
	s.push(7)
	print(s.pop())
	print(s.pop())
	print(s.pop())
	print(s.pop())
	print(s.pop())

if __name__ == '__main__':
	tests()