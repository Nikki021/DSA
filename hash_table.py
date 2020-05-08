# Implementing a hash table
# [['grapes', 10000],['apples', 500]] something like this

from random import randint

class HashTable:
	def __init__(self):
		self.data = [None]*50

	def _hash(self, key):
		val = 0
		for i in range(len(key)):
			val = (val + ord(key[i])*i) % len(self.data)
		return val

	def set(self, key, value):
		address = self._hash(key)
		if not self.data[address]:
			self.data[address] = []
		self.data[address].append([key, value])

	def get(self, key):
		address = self._hash(key)
		currentBucket = self.data[address]
		if(currentBucket):
			for i in range(len(currentBucket)):
				if currentBucket[i][0] == key:
					return currentBucket[i][1]
		return "Key doesn't exists!!"

	def keys(self):
		keysArray = []
		for i in range(len(self.data)):
			if self.data[i]:
				keysArray.append(self.data[i][0][0])
		return keysArray


h = HashTable()
h.set('grapes', 1000)
h.set('apples', 50)
h.set('oranges', 20)
h.set('berries', 25)
print(h.get('grapes'))
print(h.get('watermelons'))
print(h.data)
print(h.keys())