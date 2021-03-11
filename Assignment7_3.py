'''
Que -> Write a program which contains one class named as Numbers.
	   Arithmetic class contains one instance variables as Value.
	   Inside init method initialise that instance variables to the value which is accepted from user.
	   There are four instance methods inside class as ChkPrime(), ChkPerfect(), SumFactors(),
	   Factors().
	   ChkPrime() method will returns true if number is prime otherwise return false.
   	   ChkPerfect() method will returns true if number is perfect otherwise return false.
	   Factors() method will display all factors of instance variable.
	   SumFactors() method will return addition of all factors. Use this method in any another method
	   as a helper method if required.
	   After designing the above class call all instance methods by creating multiple objects.
'''

class Arithmetic:
	
	def __init__(self,i):
		self.value = i
		self.Factor = []

	def ChkPrime(self):
		if (self.value > 1):
			for i in range(2,int(self.value / 2)+1):
				if(self.value / i) == 0:
					return False
					break
			else:
				return True
		else:
			return False		

	def ChkPerfect(self):
		sum = 0
		for i in range(1,self.value):
			if (self.value / i) == 0:
				sum += i
		return sum == self.value

	def Factors(self):
		for i in range(1,self.value+1):
			if (self.value % i) == 0:
				self.Factor.append(i)
		print("The factors are : ",self.Factor)

	def SumFactors(self):
		sum = 0
		for i in range(len(self.Factor)):
			sum += self.Factor[i]
		return sum

def main():
	num = int(input("Enter the number : "))
	Obj1 = Arithmetic(num)

	ret = Obj1.ChkPrime()
	print("Given number is prime : ",ret)

	ret = Obj1.ChkPerfect()
	print("Given number is perfect ",ret)

	Obj1.Factors()

	ret = Obj1.SumFactors()
	print(ret)

if __name__=="__main__":
	main()