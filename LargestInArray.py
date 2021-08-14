#Largets element in Array

from numpy import empty

def MaxFromArray(brr):
    iMax=brr[0]
    for iCnt in range(len(brr)):
        if iMax < brr[iCnt] :
            iMax=brr[iCnt]

    return iMax

def main():
    print("Enter the size of the array")
    iSize=int(input())
    arr=empty(iSize)
    for iCnt in range(iSize):
        print("Enter the element",iCnt+1)
        arr[iCnt]=int(input())

    iMax=MaxFromArray(arr)
    print("Maximum element from array is:",iMax)

if __name__=="__main__":
    main()