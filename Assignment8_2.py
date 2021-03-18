'''
Que -> Design python application which creates two threads as evenfactor and oddfactor.
Both the thread accept one parameter as integer. Evenfactor thread will display
addition of even factors of given number and oddfactor will display addition of odd
factors of given number. After execution of both the thread gets completed main
thread should display message as “exit from main”.
'''

import threading


def EvenFact(no1):
    sum1 = 0
    for i in range(1, no1 + 1):
        if no1 % i == 0:
            if i % 2 == 0:
                sum1 += i
    print("Addition of even factors are : ",sum1)


def OddFact(no2):
    sum1 = 0
    for i in range(1, no2 + 1):
        if no2 % i == 0:
            if i % 2 != 0:
                sum1 += i
    print("Addition of odd factors are : ",sum1)


def main():
    ivalue = int(input("Enter the value : "))

    t1 = threading.Thread(target=EvenFact, args=(ivalue,))
    t2 = threading.Thread(target=OddFact, args=(ivalue,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main.")

if __name__ == "__main__":
    main()
