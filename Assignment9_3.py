'''
Que -> Write a program which accept file name from user and create new file named as Demo.txt and
copy all contents from existing file into new file. Accept file name through command line
arguments.
Input : ABC.txt
Create new file as Demo.txt and copy contents of ABC.txt in Demo.txt 
'''

import sys

def main():
	# Command Line Arguments.
	name = sys.argv[1]

	fobj = open(name,"r")

	name2 = sys.argv[2]
	sobj = open(name2,"a")

	for Data in fobj:
		sobj.write(Data)

	sobj = open(name,"r")

	print("Reading the copied data from first file into second file.\n")
	print(sobj.read())


if __name__=="__main__":
	main()