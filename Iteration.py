#Sequence

def StartS():
	print("Jay Ganesh")
	print("Jay Ganesh")
	print("Jay Ganesh")
	print("Jay Ganesh")
	print("Jay Ganesh")


def StartI(Value,msg="Jay Ganesh"):
	iCnt=0
	while iCnt < Value:
		print(msg)
		iCnt=iCnt+1;

def main():
	print("Output by sequence")
	StartS()
	print("Output by iteration")
	print("Enter how many times you want to iterate")
	value=int(input())
	print("Enter message you want to enter")
	message=input()
	StartI(value,message)
	print("Ouput when default parameter is used")
	print("Enter how many times you want to iterate")
	value=int(input())
	StartI(value) #Default msg
	
	

if __name__=="__main__":
	main()