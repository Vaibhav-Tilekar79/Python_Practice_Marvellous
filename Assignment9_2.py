'''
Que -> Write a program which accept file name from user and open that file and display the contents
	of that file on screen.
	Input : Demo.txt
	Display contents of Demo.txt on console.
'''

def main():
	name = input("Enter the file name : ")

	fobj = open(name,"r")

	print("The contents of the file is : \n")

	print(fobj.read())

if __name__=="__main__":
	main()