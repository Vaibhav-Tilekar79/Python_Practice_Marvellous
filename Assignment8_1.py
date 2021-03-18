'''
Que -> Design python application which creates two thread named as even and odd. Even
thread will display first 10 even numbers and odd thread will display first 10 odd
numbers.

'''

import threading

def Even(n1):
	arr = []
	for i in range(n1):
		if (i % 2) == 0:
			arr.append(i)
	print(arr)

def Odd(n2):
	arr = []
	for i in range(n2):
		if (i % 2) != 0:
			arr.append(i)
	print(arr)		

def main():
	n = 20
	t1 = threading.Thread(target = Even, args = (n,))
	t2 = threading.Thread(target = Odd, args = (n,))

	t1.start()
	t2.start()

	t1.join()
	t2.join()

if __name__=="__main__":
	main()