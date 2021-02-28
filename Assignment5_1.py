'''
Que -> Write a recursive program which display below pattern.

E.g -> Input :  5
	   Output : * * * * *
'''

def rep(no):
	if no > 0:
		print("*",end=" ")
		rep(no-1)

def main():
	nos1 = 5
	rep(nos1)

if __name__=="__main__":
	main()	