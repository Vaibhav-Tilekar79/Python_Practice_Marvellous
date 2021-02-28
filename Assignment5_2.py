'''
Que -> Write a recursive program which display below pattern.
E.g -> Input :  5
       Output : 1 2 3 4 5
'''

def output(no):
	if (no > 0):
		output(no-1)
		print(no,end=" ")	

def main():
	input = 5
	output(input)

if __name__=="__main__":
	main()