from collections import Iterable


class ClassMate(object):
	def __init__(self):
		self.names = list()

	def add(self, name):
		self.names.append(name)

	def __iter__(self):
		return ClassIterable()


class ClassIterable(object):
	def __init__(self):
		pass

	def __next__(self):
		pass


cm = ClassMate()

cm.add('focsudroid')
cm.add('roid')
cm.add('focsud')

print(isinstance(cm, Iterable))
print(cm)


