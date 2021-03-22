'''
Que -> Write a program which accept two file names from user and compare contents of both the
files. If both the files contains same contents then display success otherwise display failure.
Accept names of both the files from command line.
Input : Demo.txt Hello.txt
Compare contents of Demo.txt and Hello.txt
'''

import filecmp

def main():
	name1 = input("Enter first file name to read : ")
	
	name2 = input("Enter the second file name to read: ")

	result = filecmp.cmp(name1,name2)

	if result == True:
		print("Contents of both the files are same.")
	else:
		print("Contents of both the files are different.")	

if __name__=="__main__":
	main()