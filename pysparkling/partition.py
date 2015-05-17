import itertools


class Partition(object):
	def __init__(self, x, idx=None):
		self.index = idx
		self._x = x

	def x(self):
		self._x, r = itertools.tee(self._x)
		return r

	def hashCode(self):
		return self.index
