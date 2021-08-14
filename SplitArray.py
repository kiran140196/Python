from numpy import empty
from numpy import delete

def SplitArray(arr):
    print("Enter at which position you want to split the array")
    iSplit=int(input())

    temp=empty(iSplit)
    for iCnt in range(iSplit):
        temp[iCnt]=arr[iCnt]

    print("Contents of temp are:")
    print(temp)
    print(arr)

    index=iSplit
    for iCnt in range(index,len(arr),1):
       arr[iCnt-iSplit]=arr[iCnt]

    print(arr)
    iCnt3=0
    for iCnt in range(index,len(arr)):
        arr[iCnt]=temp[iCnt3]
        iCnt3+=1

 
    print("Contents of array after spliting and adding it to end")
    print(arr)

def main():
    print("Enter the no of elements")
    iSize=int(input())
    arr=empty(iSize)
    for iCnt in range(iSize):
        print("Enter the element",iCnt+1)
        arr[iCnt]=int(input())

    SplitArray(arr)


if __name__=="__main__":
    main()