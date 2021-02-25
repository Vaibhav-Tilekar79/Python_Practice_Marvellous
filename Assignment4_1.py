'''
Que -> Write a program which contains one lambda function which accepts one parameter and return
       power of two.
E.g -> Input : 4 
	   Output : 16
'''

Raiseto = lambda no : no**2

def main():
	inp = int(input("Enter the number : "))

	ret = Raiseto(inp)

	print(ret)

if __name__=="__main__":
	main()