'''
Que -> Write a program which display 10 to 1 on screen.

E.g -> Output : 10 9 8 7 6 5 4 3 2 1
'''
def DecrementNo():
	no = 10
	for i in range(no, 0, -1):
		print(i, end=" ")	

def main():
	DecrementNo()

if __name__=="__main__":
	main()