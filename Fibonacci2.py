
def Fib(iNo):
    arr=[0]*(iNo+1)
    arr[0]=0
    print(arr[0],end=" ")
    arr[1]=1
    iCnt=2
    print(arr[1],end=" ")
    while iCnt!=iNo+1:
        arr[iCnt]=arr[iCnt-1]+arr[iCnt-2]
        print(arr[iCnt],end=" ")
        iCnt +=1

def main():
    print("Enter the no")
    iNo=int(input())
    Fib(iNo)

if __name__=="__main__":
    main()