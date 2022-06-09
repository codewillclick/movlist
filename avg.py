#!/bin/env python3

from .rot import rotlist

class avglist:
	def __init__(self,table,default=0):
		self._table = dict(table)
		self._size = max(*([1]+list(self._table.values()))) + 1
		self._arr = rotlist(self._size,default)
		self._sums = {k:(default*(v+1)) for k,v in self._table.items()}
	
	def __len__(self):
		return len(self._arr)
	
	def __iter__(self):
		return iter(self._arr)
	
	def add(self,val):
		print('adding',val)
		print(list(self))
		print('sums before: ',self._sums)
		for k,v in self._table.items():
			# Pull offset from the end of the list.
			old = self._arr[len(self)-1-v]
			print(':',k,'old',old,'new',val)
			self._sums[k] -= old
			self._sums[k] += val
		print('sums after:  ',self._sums,'\n')
		self._arr.add(val)
	
	def sums(self):
		return dict(self._sums)
	
	def avg(self):
		return {k:(v/(self._table[k]+1)) for k,v in self._sums.items()}

