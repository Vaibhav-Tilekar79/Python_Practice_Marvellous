'''
Que -> Write a program which accept one number for user and check whether number is prime or not.

E.g -> Input : 5    
	   Output : It is Prime Number
'''

def IsPrime(nos):
	flag = 0
	if (nos <= 1):
		flag = 1
		print("It is not a prime number.")
	else:
		for i in range(2,nos):
			if (nos % i == 0):
				flag = 1
				print(nos, "It is not a prime number.")
		if flag == 0:
			print(nos, "Is a prime number.")
			
	# if (nos<=1):
	# 	print("It is not a prime number.")
	# else:
	# 	for i in range(2,nos):	
	# 		if (nos % i == 0):
	# 			print(nos, "Is not a prime number.")
	# 			break
	# 	else:
	# 		print(nos, "Is a prime number.")			

def main():
	IntNum = int(input("Enter the number: "))
	IsPrime(IntNum)

if __name__=="__main__":
	main()