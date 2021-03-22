'''
Que -> Accept file name and one string from user and return the frequency of that string from file.
Input : Demo.txt Marvellous
Search “Marvellous” in Demo.txt
'''

def main():
	name1 = input("First file name : ")
	fobj = open(name1,"r")

	name2 = input("String to check frequency : ")

	count = 0

	for line in fobj:
		if name2 in line:
			count += 1
	else:
		print("No such string present.")

	print("Total number of repitations is : ",count)

if __name__=="__main__":
	main()