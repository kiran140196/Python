def Addition(arr):
	iSum=0
	for iCnt in range(len(arr)):iSum=iSum+arr[iCnt]
	return iSum

iSum1=0
i=0
def AdditionR(arr):
	global iSum1
	global i
	if i< len(arr):
		iSum1=iSum1+arr[i]
		i=i+1
		AdditionR(arr)
	return iSum1
	
def main():
	arr=[]
	
	iSize=int(input("Enter the size of array"))

	for iCnt in range(iSize):arr.append(int(input()))

	print("Entered Data is:",arr)

	print("Adddition is:",Addition(arr))

	print("Additon by r",AdditionR(arr))

	

if __name__=="__main__":
	main()