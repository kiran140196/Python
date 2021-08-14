#Find the nth fibonacci 
from numpy import empty

def Fib(iEnd):
    iCnt=3
    arr=empty(iEnd+1)
    arr[0]=0
    print(int(arr[0]),end=" ")
    arr[1]=1
    while iCnt != iEnd+1:
        arr[iCnt]=arr[iCnt-1]+arr[iCnt-2]
        print(int(arr[iCnt]),end=" ")
        iCnt +=1

def main():
    print("Enter the no till which you want fibonacci series")
    iEnd=int(input())
    if iEnd < 0:
        print("Enter the valid number")
    Fib(iEnd)

if __name__=="__main__":
    main()