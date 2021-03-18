'''
Que -> Design python application which creates three threads as small, capital, digits. All the
threads accepts string as parameter. Small thread display number of small characters,
capital thread display number of capital characters and digits thread display number of
digits. Display id and name of each thread.
'''

import threading

def smallChar(str1):
	count = 0
	for i in str1:
		if i.islower():
			count += 1
	print("Total count of small characters is : ",count)
	
def capChar(str2):
	count = 0
	for i in str2:
		if i.isupper():
			count += 1
	print("Total count of Capital characters is : ",count)

def digChar(str3):
	count = 0
	for i in str3:
		if i.isnumeric():
			count += 1
	print("Total count of digits is : ",count)								

def main():
	stringIn = input("Enter the string : ")

	small = threading.Thread(target = smallChar, args = (stringIn, ))
	capital = threading.Thread(target = capChar, args = (stringIn, ))
	digits = threading.Thread(target = digChar, args = (stringIn, ))

	small.start()
	capital.start()
	digits.start()

	small.join()
	capital.join()
	digits.join()

if __name__=="__main__":
	main()