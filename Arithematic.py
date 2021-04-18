#Defination of addition function
def Addition(no1,no2):
	ans=no1+no2
	return ans


#Defination of Subtraction function
def Subtraction(no1,no2):
	ans=no1-no2
	return ans


#entry point function
def main():
	print("Enter first number:")
	value1=int(input())
	print("Enter second number:")
	value2=int(input())

	ret1=Addition(value1,value2)
	ret2=Subtraction(value1,value2)

	print("Addition is:",ret1)
	print("Subtraction is:",ret2)	

#Code starter
if __name__=="__main__":
	main()


