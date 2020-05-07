# we have two sorted arrays and we have to merge them to single sorted array
# [12,15,18,20] [1,5,17,21]
# [1,5,12,15,17,18,20,21]

def merge(arr1, arr2):
	myList = []
	i = 0
	j = 0
	while(i < len(arr1) or j < len(arr2)):
		if(i == len(arr1) and j < len(arr2)):
			myList.append(arr2[j])
			j += 1
		elif(j == len(arr2) and i < len(arr1)):
			myList.append(arr1[i])
			i += 1
		elif(arr1[i] < arr2[j]):
			myList.append(arr1[i])
			i += 1
		else:
			myList.append(arr2[j])
			j += 1
	return myList

a1 = [12,15,18,20,25,27]
a2 = [1,5,17,21,22,23,26,30,31,33]
print(merge(a1, a2))