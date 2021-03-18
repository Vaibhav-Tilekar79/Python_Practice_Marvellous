'''
Que -> Design python application which creates two threads as evenlist and oddlist. Both the
threads accept list of integers as parameter. Evenlist thread add all even elements
from input list and display the addition. Oddlist thread add all odd elements from input
list and display the addition.
'''

import threading


def EvenList(size1, arr1):
    sum = 0
    for i in range(size1):
        if (arr1[i] % 2 == 0):
            sum += arr1[i]
    print("The addition of all even number is : ",sum)


def OddList(size1, arr1):
    sum = 0
    for i in range(size1):
        if (arr1[i] % 2 != 0):
            sum += arr1[i]
    print("The addition of all even number is : ",sum)


def main():
    size = int(input("Enter the size of list : "))
    arr = []

    for i in range(size):
        print("Enter element : ", i + 1)
        num = int(input())
        arr.append(num)

    t1 = threading.Thread(target=EvenList, args=(size, arr,))
    t2 = threading.Thread(target=OddList, args=(size, arr,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()


if __name__ == "__main__":
    main()
