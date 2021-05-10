class Marvellous:
	iValue1=11		#Class/Static charchteristic

	def __init__(self,iNo1,iNo2):		#Constructor
		print("Inside Constructor")	#instance variable
		self.i=iNo1
		self.j=iNo2

	def __del__(self):		#Destructor
		print("Inside Destructor")

	def Fun(self):				#instance method
		print("Inside Fun method")
		print("Value of j is:",self.j)

def main():
	obj1=Marvellous(11,21)		#creating the object
	obj2=Marvellous(51,101)

	print("Value of i from obj1:",obj1.i)	#Accessing instance members
	print("Value of i from obj2:",obj2.i)
	print("Vlaue of class member:",Marvellous.iValue1)	#Accessing class members
	obj1.Fun()		#calling instance method
	obj2.Fun()
	del obj1		#dellocating the memory of object
	del obj2

if __name__=="__main__":
	main()