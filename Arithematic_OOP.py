class Arithematic:     #Class Defination	
	Value=111	#Class Variable
	def __init__(self,iNo1,iNo2):   #Class Constructor
		print("Inside Constructor")
		self.iValue1=iNo1   	# Instance variable
		self.iValue2=iNo2    	# Instance variable

	def Add(self):                  #Instance method
		print(self.Value)
		return self.iValue1+self.iValue2

	def Sub(self):                  #Instance method
		return self.iValue1-self.iValue2

def main():
	print("Value is:",Arithematic.Value)

	obj=Arithematic(21,11) 		#__init__(obj,21,11)
	obj2=Arithematic(101,51)	#__init__(obj2,101,51)

	ret=obj.Add()
	print("Addition is:",ret)
	ret=obj.Sub()          		#ret=Sub(obj)
	print("Subtraction is:",ret)
	print("Value is:",obj.Value)

	ret=obj2.Add()
	print("Addition is:",ret)
	ret=obj2.Sub()
	print("Subtraction is:",ret)
	print("Value is:",obj2.Value)


if __name__=="__main__":
	main()