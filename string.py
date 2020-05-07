# create a function to reverse a string
# for example: if given string is "Hi I am Nikhil"
# it should return "lihkiN ma I iH"

def reverse(s):
	myList = []
	for i in range(len(s)):
		myList.append(s[len(s)-1-i])
	return ''.join(myList)

s1 = "Hi I am Nikhil"
print(reverse(s1))
print(s1[::-1])