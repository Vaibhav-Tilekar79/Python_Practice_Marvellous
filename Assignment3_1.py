'''
Que -> Write a program which accept N numbers from user and store it into List. Return addition of all
	   elements from that List.

E.g ->	Input : Number of elements : 6
		Input Elements : 13 5 45 7 4 56
		Output : 130
'''

def Add(value):
	sum = 0
	for i in range(len(value)):
		sum = sum + value[i]
	return sum

def main():
	arr = []
	size = int(input("Enter total number of elements : "))

	for i in range(size):
		print("Enter number : ",i+1)
		num = int(input())
		arr.append(num)

	print("Entered input is : ",Arr)

	ret = Add(arr)	
	print("The addition is : ",ret)

if __name__=="__main__":
	main()