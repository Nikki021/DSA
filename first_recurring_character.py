# lets say we have an array [1,3,2,5,2,12,4,2]
# we need to find the first recurring character, in this case 2

def FirstRecurringCharacter1(array):
	for i in range(len(array)):
		for j in range(i+1, len(array)):
			if array[i] == array[j]:
				return array[i]
	return None

def FirstRecurringCharacter2(array):
	store = [None]*100
	for i in range(len(array)):
		if store[array[i]] is not None:
			return array[i]
		else:
			store[array[i]] = i
	return None

print(FirstRecurringCharacter1([2,5,5,1,2,6,7]))
print(FirstRecurringCharacter2([2,5,5,1,2,6,7]))