'''
Que -> Write a program which accept N numbers from user and store it into List. Return Maximum
	   number from that List.

E.g ->	Input : Number of elements : 7
		Input Elements : 13 5 45 7 4 56 34
		Output : 56
'''


def FindMax(LIST):
	#return max(LIST)
	max = LIST[0]
	for i in LIST:
		if i > max:
			max = i
	return max		


def main():
	Arr = []
	size = int(input("Enter the number of elements : "))

	for i in range(size):
		print("Enter the element : ",i+1)
		no = int(input())
		Arr.append(no)

	print("Entered input is : ",Arr)	

	ret = FindMax(Arr)

	print("The maximum number in given list is : ",ret)

if __name__=="__main__":
	main()