'''
Que -> Write a program which contains one class named as BankAccount.
	BankAccount class contains two instance variables as Name & Amount.
	That class contains one class variable as ROI which is initialise to 10.5.
	Inside init method initialise all name and amount variables by accepting the values from user.
	There are Four instance methods inside class as Display(), Deposit(), Withdraw(),
	CalculateIntrest().
	Deposit() method will accept the amount from user and add that value in class instance variable
	Amount.
	Withdraw() method will accept amount to be withdrawn from user and subtract that amount
	from class instance variable Amount.
	CalculateIntrest() method calculate the interest based on Amount by considering rate of interest
	which is Class variable as ROI.
	And Display() method will display value of all the instance variables as Name and Amount.
	After designing the above class call all instance methods by creating multiple objects.
'''

class BankAccount:
	ROI = 10.5

	def __init__(self,i):
		self.name = i
		self.amount = 0

	def Deposit(self):
		amt = int(input("Enter the amount you want to deposit : "))
		self.amount += amt
		print("Your Total balance amount is : ",self.amount)

	def Withdraw(self):
		witdrw = int(input("Enter the amount you want to withdraw : "))
		self.amount -= witdrw
		print("Your Total balance amount is : ",self.amount)

	def CalculateIntrest(self):
		print("Rate of Interest : ",BankAccount.ROI)

	def Display(self):
		print("Name is : ",self.name)
		print("Amount is : ",self.amount)

def main():
	name1 = input("Enter your name : ")
	Obj1 = BankAccount(name1)

	Obj1.Deposit()
	Obj1.Withdraw()	
	Obj1.CalculateIntrest()

	name2 = input("Enter your name : ")
	Obj2 = BankAccount(name2)

	Obj2.Deposit()
	Obj2.Withdraw()	
	Obj2.CalculateIntrest()

	name2 = input("Enter your name : ")
	Obj3 = BankAccount(name2)

	Obj3.Deposit()
	Obj3.Withdraw()	
	Obj3.CalculateIntrest()

if __name__=="__main__":
	main()