#function accepts nothing and return nothing
def fun():
	print("Function fun")

#function which accepts paramter and and return nothing
def gun(no):
	print("Function gun with parameter:",no)

#function which accepts parameter and return the value
def sun(no):
	print("Function sun with parameter:",no)
	return no+1

#function accpets multiple value and return multiple value
def AddSub(no1,no2):
	add=no1+no2
	sub=no1-no2
	return add,sub

def mun():
	pass	

#Nested functions defination
def Marvellous():
	print("Inside Marvellous")
	def Infosystems():
		print("Inside Infosystems")
	Infosystems()
	Infosystems()
	

def main():
	fun()	
	gun(11)
	ret=sun(11)
	print("Return value of sun is:",ret)

	ret1,ret2=AddSub(20,10)
	print("Addition is:",ret1)
	print("Subtraction is:",ret2)

	Marvellous()
	mun()

if __name__=="__main__":
	main()