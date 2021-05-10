#Consider inbulit function from module
def Subtraction(iNo1,iNo2):		#100
	return iNo1 - iNo2

def SubDecorator(fun_name):		#200   #fun_name=100
	def Updater(iValue1,iValue2):	#300
		if iValue1 < iValue2:
			iValue1,iValue2=iValue2,iValue1
		return fun_name(iValue1,iValue2) # return call 100(10,6)

	return Updater			#return 300


def main():				#400

	sub=SubDecorator(Subtraction)  #call 200(100)  #sub contains 300
	print("Enter first no")
	iValue1=int(input())		#iValue1=6
	print("Enter second no")
	iValue2=int(input())		#iValue2=10
	ret=sub(iValue1,iValue2)	#call 300(6,10) #ret will contain value from return fun_name(iValue1,iValue2)
	print("Subtraction is:",ret)

if __name__=="__main__":
	main()				#call 400