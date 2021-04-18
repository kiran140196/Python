def DisplayF(Value):
	print("Output of for loop")
	iCnt=0
	for iCnt in range(0,Value):
		print("Jay Ganesh")

def DisplayW(Value):
	print("Output of while loop")
	iCnt=0;
	while iCnt < Value:
		print("Jay Ganesh")
		iCnt=iCnt+1
	
def main():
	print("Enter the no of iterations")
	no=int(input())

	DisplayF(no)
	DisplayW(no)

if __name__=="__main__":
	main()