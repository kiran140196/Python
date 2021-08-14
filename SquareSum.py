def Square(iNo):
    return iNo*iNo

def SumOfSquare(iValue):
    iSum=0
    for iCnt in range(iValue+1):
        iSum=iSum+Square(iCnt)
    
    return iSum

def main():
    print("Enter till which number you want sum of square")
    iValue=int(input())
    iRes=SumOfSquare(iValue)
    print("Sum of square is:",iRes)


if __name__=="__main__":
    main()