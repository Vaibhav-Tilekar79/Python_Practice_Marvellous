'''
Que -> Write a program which contains filter(), map() and reduce() in it. Python application which
	   contains one list of numbers. List contains the numbers which are accepted from user. Filter
	   should filter out all prime numbers. Map function will multiply each number by 2. Reduce will
	   return Maximum number from that numbers. (You can also use normal functions instead of
	   lambda functions).

E.g -> Input List = [2, 70 , 11, 10, 17, 23, 31, 77]
	   List after filter = [2, 11, 17, 23, 31]
	   List after map = [4, 22, 34, 46, 62]
	   Output of reduce = 62

'''
import functools

def ChkPrime(list1):
	flag = 0
	if (list1 <= 1):
		flag = 1
		return False
	else:
		for j in range(2, list1):
			if (list1 % j == 0):
				flag = 1
		if flag == 0:
			return True
		else:
			return False			

def Mul(no1):
	return (no1 * 2)

def MaxN(no1,no2):
	max = 0
	if no1 > no2:
		max = no1
	else:
		max = no2
	return max	

def main():
	arr = []
	size = int(input("Enter the number of elements : "))

	for i in range(size):
		print("Enter the elements : ",i+1)
		no = int(input())
		arr.append(no)
	
	print("Entered data is : ",arr)

	f1 = list(filter(ChkPrime,arr))	
	print("List after filter : ",f1)

	m1 = list(map(Mul,f1))
	print("List after map : ",m1)

	r1 = functools.reduce(MaxN,m1)
	print("Output of reduce : ",r1)

if __name__=="__main__":
	main()