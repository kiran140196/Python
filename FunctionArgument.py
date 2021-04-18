#Positional arguments
def Student(name,no,address,marks):
	print("Name of student is:",name)
	print("Roll no is:",no)
	print("Address is:",address)
	print("Marks is:",marks)


#Keyword arguments
def Computer(RAM,Processor,HDD):
	print("RAM size is:",RAM)
	print("Processor name is:",Processor)
	print("Size of HDD is:",HDD)

#Default arguments
def CircleArea(Radius,PI=3.14):
	print("Value of PI is:",PI)
	return PI*Radius*Radius

#Variable no of arguments
def fun(*Value):
	print("Number of arguments are:",len(Value))

def main():
	Student("Kiran",21,"Pune",98)
	Computer(Processor="i7",RAM=16,HDD="2TB")
	Computer(RAM=8,HDD="1TB",Processor="i5")
	CircleArea(10.25,6.25)
	CircleArea(10.25)
	fun(10,20,30)
	fun(11,21,31,41,51)
	fun()

if __name__=="__main__":
	main()