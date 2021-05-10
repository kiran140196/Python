#Accept n no from user and filter out only even no from that n no 
#After that add 2 in every even number
#After that perform summation of that modified number

#Input[1,3,2,4,6,5,4]
#After filter[2,4,6,4]
#After map[4,6,8,6]
#After reduce 24

import functools

def main():
	arr=[]
	print("Enter the no of elements")
	iSize=int(input())

	for iCnt in range(iSize):
		print("Enter the element",iCnt+1)
		iNo=int(input())
		arr.append(iNo)
	print("Your entered data is:",arr)

	#newData=filter(function_name,Data)
	newData=list(filter(lambda iNo : iNo % 2 == 0,arr))               
	print("Your filtered data is:",newData)

	newMapData=list(map(lambda iNo : iNo+2,newData))	          
	print("After map data is:",newMapData)

	iSum=functools.reduce(lambda iNo1,iNo2 : iNo1+iNo2,newMapData)		  
	print("After reduce result is:",iSum)

if __name__=="__main__":
	main()