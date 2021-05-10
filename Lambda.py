#named function
def Addition(iNo1,iNo2):
	return iNo1+iNo2

#lambda function
Sum=lambda iNo1,iNo2 : iNo1+iNo2

def fun(name):
	iRet=name(10,20)
	print("Value form fun is:",iRet)

def main():
	print("Enter first number")
	iNo1=int(input())

	print("Enter second number")
	iNo2=int(input())
	
	iRet=Addition(iNo1,iNo2)
	print("Addition is:",iRet)

	iRet=Sum(iNo1,iNo2)
	print("Addition with lambda is:",iRet)

	fun(Sum)

if __name__=="__main__":
	main()