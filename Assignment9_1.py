'''
Que -> Write a program which accepts file name from user and check whether that file exists in
	   current directory or not.
	   Input : Demo.txt
	   Check whether Demo.txt exists or not.
'''

import os

def main():
	name = input("Enter file name that you want to check : ")

	ifExists = os.path.isfile(name)

	if ifExists == True:
		print("Given file is already present.")
	else:
		print("No such file exists.")

if __name__=="__main__":
	main()