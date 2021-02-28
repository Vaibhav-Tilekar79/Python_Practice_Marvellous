'''
Que -> Write a recursive program which display below pattern.
E.g -> Input :  5
	   Output : 5 4 3 2 1
'''


def output(no):
	if (no > 0):
		print(no,end=" ")
		output(no-1)

def main():
	input = 5
	output(input)

if __name__=="__main__":
	main()