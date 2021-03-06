from collections import Iterable
from collections import Iterator
import time

class ClassMate(object):
	def __init__(self):
		self.names = list()
		self.current_num = 0


	def add(self, name):
		self.names.append(name)

	def __iter__(self):
		return self

	def __next__(self):
		if self.current_num < len(self.names):
			ret = self.names[self.current_num]
			self.current_num += 1
			return ret
		else:
			raise StopIteration

cm = ClassMate()


cm.add('wangxu')
cm.add('focusdroid')
cm.add('tree')
cm.add('focus')

# print('', isinstance(cm, Iterable))
# cm_iterator = iter(cm)
# print(isinstance(cm_iterator, Iterator))

for temp in cm:
	print(temp)
	time.sleep(1)