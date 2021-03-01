'''
Que -> Write a program which contains one class named as Arithmetic.
Arithmetic class contains three instance variables as Value1 ,Value2.
Inside init method initialise all instance variables to 0.
There are three instance methods inside class as Accept(), Addition(), Subtraction(),
Multiplication(), Division().
Accept method will accept value of Value1 and Value2 from user.
Addition() method will perform addition of Value1 ,Value2 and return result.
Subtraction() method will perform subtraction of Value1 ,Value2 and return result.
Multiplication() method will perform multiplication of Value1 ,Value2 and return result.
Division() method will perform division of Value1 ,Value2 and return result.
After designing the above class call all instance methods by creating multiple objects.
'''

class Arithmetic:

	def __init__(self):
		self.Value1 = 0
		self.Value2 = 0

	def Accept(self):
		no1 = int(input("Enter the first value : "))
		self.Value1 = no1
		no2 = int(input("Enter the second value : "))
		self.Value2 = no2

	def Addition(self):
		return (self.Value1 + self.Value2)

	def Substraction(self):
		return (self.Value1 - self.Value2)

	def Multiplication(self):
		return (self.Value1 * self.Value2)

	def Division(self):
		return (self.Value1 / self.Value2)

def main():
	Obj1 = Arithmetic()
	Obj1.Accept()
	
	ret = Obj1.Addition()
	print("Addition of given numbers are : ",ret)
	ret = Obj1.Substraction()
	print("Substraction of given numbers are : ",ret)
	ret = Obj1.Multiplication()
	print("Multiplication of given numbers are : ",ret)
	ret = Obj1.Division()
	print("Division of given numbers are : ",ret)

	Obj2 = Arithmetic()
	Obj2.Accept()
	
	ret = Obj2.Addition()
	print("Addition of given numbers are : ",ret)
	ret = Obj2.Substraction()
	print("Substraction of given numbers are : ",ret)
	ret = Obj2.Multiplication()
	print("multiplication of given numbers are : ",ret)
	ret = Obj2.Division()
	print("Division of given numbers are : ",ret)

if __name__=="__main__":
	main()