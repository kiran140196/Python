#Accept n no from user and filter out only even no from that n no 
#After that add 2 in every even number
#After that perform summation of that modified number

#Input[1,3,2,4,6,5,4]
#After filter[2,4,6,4]
#After map[4,6,8,6]
#After reduce 24

def CheckEven(iNo):
	if iNo % 2 == 0:
		return True
	else :
		return False

def Filter(arr):
	brr=[]
	for iCnt in range(len(arr)):
		if CheckEven(arr[iCnt]) == True:
			brr.append(arr[iCnt])
	return brr

def Map(newData):
	crr=[]
	for iCnt in range(len(newData)):
		iNewEle=newData[iCnt]+2
		crr.append(iNewEle)
	return crr
		

def Reduce(newMapData):
	iSum=0
	for iCnt in range(len(newMapData)):
		iSum=iSum+newMapData[iCnt]
	return iSum

def main():
	arr=[]
	print("Enter the no of elements")
	iSize=int(input())

	for iCnt in range(iSize):
		print("Enter the element",iCnt+1)
		iNo=int(input())
		arr.append(iNo)
	print("Your entered data is:",arr)

	newData=Filter(arr)
	print("Your filtered data is:",newData)

	newMapData=Map(newData)
	print("After map data is:",newMapData)

	iSum=Reduce(newMapData)
	print("After reduce result is:",iSum)

if __name__=="__main__":
	main()