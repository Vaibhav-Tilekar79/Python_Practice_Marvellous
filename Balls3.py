'''
Classifier : Decision Tree
DataSet : Balls Dataset
Features : Weight & Surface type
Labels : Tennis and Cricket
Training Dataset : 15 Entries
Testing Dataset : 1 Entry
'''
from sklearn import tree
# Rough -> 1
# Smooth -> 0
# Tennis -> 1
# Cricket -> 2

def MarvellousML(weight,surface):
	# Step 1 & 2
			#	[Weight,Surface]
	Features = [[35,1],[47,1],[90,0],[48,1],
				[90,0],[35,1],[92,0],[35,1],
				[35,1],[35,1],[96,0],[43,1],
				[110,0],[35,1],[95,0]]

	Labels = [1,1,2,1,
			  2,1,2,1,
			  1,1,2,1,
			  2,1,2]

	# Step 3
	dobj = tree.DecisionTreeClassifier()

	# Step 4 -> Train the data
	dobj = dobj.fit(Features,Labels)

	# Step 5 -> Predict the data
	result = dobj.predict([[weight,surface]])

	if result == 1:
		print("Your object looks like Tennis Ball")
	elif result == 2:
		print("Your object looks like Cricket Ball")

def main():
	print("-----Program to Train and Predict the Ball by Decision Tree-----")
	print("--------------- Supervised Machine Learning ---------------")
	
	print("Enter Weight of object : ")
	weight = int(input())
	print("Enter surface type of object : ")
	surface = input()

	if surface.lower() == "rough":
		surface = 1
	elif surface.lower() == "smooth":
		surface = 0
	else:
		print("Invalid input")
		return

	MarvellousML(weight, surface)

if __name__=="__main__":
	main()
