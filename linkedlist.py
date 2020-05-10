class Node:
	def __init__(self, value):
		self.value = value
		self.next = None

class LinkedList:
	def __init__(self, value):
		self.head = Node(value)
		self.tail = self.head
		self.length = 1

	def append(self, value):
		newNode = Node(value)
		self.tail.next = newNode
		self.tail = newNode
		self.length += 1

	def prepend(self, value):
		newNode = Node(value)
		newNode.next = self.head
		self.head = newNode
		self.length += 1

	def traverseToIndex(self, index):
		if index == 0:
			return self.head
		i = 0
		tempNode = self.head
		prevNode = None
		while(i != index):
			prevNode = tempNode
			tempNode = tempNode.next
			i += 1
		return prevNode

	def insert(self, index, value):
		newNode = Node(value)
		if index == 0:
			return self.prepend(value)
			# newNode.next = self.head
			# self.head = newNode
			# self.length += 1
		elif index >= self.length:
			return self.append(value)
		else:
			tempNode = self.head
			prevNode = None
			i = 0
			while(i != index):
				prevNode = tempNode
				tempNode = tempNode.next
				i += 1
			newNode.next = tempNode
			prevNode.next = newNode
			self.length += 1

	def remove(self, index):
		prevNode = self.traverseToIndex(index)
		unwantedNode = prevNode.next
		prevNode.next = unwantedNode.next
		self.length -= 1

	def getNodeAt(self, index):
		prevNode = self.traverseToIndex(index)
		reqNode = prevNode.next
		return reqNode.value

	def PrintList(self):
		node = self.head
		while(node is not None):
			print(str(node.value) + " --> ", end = "")
			node = node.next

myLinkedList = LinkedList(10)
myLinkedList.append(5)
myLinkedList.prepend(12)
myLinkedList.prepend(16)
myLinkedList.append(13)
myLinkedList.insert(1,18)
myLinkedList.insert(0,22)
myLinkedList.insert(200,25)
print(myLinkedList.getNodeAt(3))
myLinkedList.remove(3)
print(myLinkedList.getNodeAt(3))
# print(myLinkedList.head.next.value)
myLinkedList.PrintList()