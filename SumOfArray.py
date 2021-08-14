#Sum of all the elements in array

from numpy import empty

def SumOfArray(iSize):
    arr=empty(iSize)
    iSum=0
    for iCnt in range(0,iSize):
        print("Enter the element",iCnt +1)
        arr[iCnt]=(int(input()))

    for iCnt in range(0,iSize):
        iSum=iSum+arr[iCnt]

    return iSum

def main():
    print("Enter how mamy elements you want in array")
    iSize=int(input())
    iRes=SumOfArray(iSize)
    print("Sum of all the elements in array is:",iRes)

if __name__=="__main__":
    main()