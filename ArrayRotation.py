#Array Rotation to Left

from numpy import empty

def RotateArray(arr):
    temp=empty(len(arr))
    print("Enter by how many elements do you want to rotate the array")
    iRotate=int(input())
    iCnt=0
    iCnt2=0
    for iCnt in range(iCnt+iRotate,len(arr)):
        temp[iCnt2]=arr[iCnt]
        iCnt2 +=1

    for iCnt3 in range(iRotate):
        temp[iCnt2]=arr[iCnt3]
        iCnt2 +=1

    return temp

def main():
    print("Enter the size of the array")
    iSize=int(input())
    arr=empty(iSize)
    for iCnt in range(iSize):
        print("Enter the element",iCnt+1)
        arr[iCnt]=int(input())

    brr=RotateArray(arr)
    print("Array after rotation")
    print(brr)

if __name__=="__main__":
    main()