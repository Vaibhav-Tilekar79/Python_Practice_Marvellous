'''
Que -> Write a program which accept name from user and display length of its name.

E.g -> Input : Marvellous Output : 10 
'''

def StrLen(nam1):
	print("The length of given string is {}.".format(len(nam1)))

def main():
	name = input("Enter the string: ")
	StrLen(name)

if __name__=="__main__":
	main()