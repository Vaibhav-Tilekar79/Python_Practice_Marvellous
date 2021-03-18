'''
Que -> Design python application which contains two threads named as thread1 and thread2.
Thread1 display 1 to 50 on screen and thread2 display 50 to 1 in reverse order on
screen. After execution of thread1 gets completed then schedule thread2.
'''

import threading

def serial1(inum,lock1):
	lock1.acquire()
	for i in range(1,inum+1):
		print(i)
	print("*****")	
	lock1.release()	

def reverse1(inum,lock2):
	lock2.acquire()
	for i in range(inum,0,-1):
		print(i)
	lock2.release()		

def main():
	no1 = 50

	lock = threading.Lock()

	thread1 = threading.Thread(target = serial1, args = (no1,lock, ))
	thread2 = threading.Thread(target = reverse1, args = (no1,lock, ))

	thread1.start()
	thread2.start()

	thread1.join()
	thread2.join()

if __name__=="__main__":
	main()