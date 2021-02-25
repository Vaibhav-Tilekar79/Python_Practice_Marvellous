'''
Que -> Write a program which display first 10 even numbers on screen.

E.g - > Output : 2 4 6 8 10 12 14 16 18 20
'''
def IsEven(num):
	for i in range(1,num+1):
		if(i % 2 == 0):
			print(i,end=" ")


def main():
	IntNum = 20
	IsEven(IntNum)

if __name__=="__main__":
	main()