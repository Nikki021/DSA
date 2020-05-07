class MyArray:
	def __init__(self):
		self.length = 0
		self.data = []

	# def __str__(self):
	# 	return str(self.__dict__)

	def get(self, index):
		return self.data[index]

	def push(self, item):
		self.data.append(item)
		self.length += 1
		return self.length

	def pop(self):
		del self.data[self.length-1]
		self.length -= 1

	def delete(self, index):
		for i in range(index, self.length-1):
			self.data[i] = self.data[i+1]
		del self.data[self.length-1]
		self.length -= 1

arr = MyArray()
#print(arr.get(0))
arr.push(12)
arr.push(11)
arr.push(10)
print(arr.get(1))
# arr.pop()
arr.delete(1)
print(arr.data)