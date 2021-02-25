'''
Que -> Write a program which display 5 times Marvellous on screen. 

E.g -> Marvellous
	   Marvellous
	   Marvellous
	   Marvellous
	   Marvellous
'''

def display(message="MARVELLOUS"):
	icnt = 5
	for i in range(icnt):
		print(message)


def main():
	display()

if __name__=="__main__":
	main()