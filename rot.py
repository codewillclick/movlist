#!/bin/env python3

class rotlist:
	def __init__(self,size,default=None):
		self._x = 0
		self._arr = [default] * size
	
	def __len__(self):
		return len(self._arr)
	
	def __getitem__(self,k):
		return self._arr[self._index(k)]
	
	def __setitem__(self,k,v):
		self._arr[self._index(k)] = v
	
	def __getattr__(self,k):
		try:
			return rotlist._attrs[k](self)
		except KeyError as e:
			raise AttributeError('no attribute (%s)' % (str(k),))
	
	def __iter__(self):
		for i in range(self.size):
			yield self[i]
	
	def _index(self,i):
		return (self._x+i) % len(self._arr)
	
	def add(self,v):
		''' Add an item to the end of the list, returning the old value. '''
		i = self._index(0)
		old = self._arr[i]
		self._arr[i] = v
		self._x += 1
		return old
	
	def set(self,k,v):
		''' Set an item at an index, returning the old value. '''
		i = self._index(k)
		old = self._arr[i]
		self._arr[i] = v
		return old

rotlist._attrs = {
	'size':lambda r:len(r._arr)
}

