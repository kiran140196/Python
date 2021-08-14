#Check whether no is armstrong no or not

def ChkArmStrongNo(iNo):
    iSum=0
    temp=iNo
    while temp !=0:
        iDigit=int(temp%10)
        iDigit=iDigit*iDigit*iDigit
        iSum=iSum+iDigit
        temp=temp/10

    print(iSum)
    if iNo == iSum :
        return True
    else :
        return False

def main():
    print("Enter the no")
    iNo=int(input())
    bRet=ChkArmStrongNo(iNo)
    if bRet == True:
        print("{} is Armstrong number".format(iNo))
    else:
        print("{} is not Armstrong number".format(iNo))

if __name__=="__main__":
    main()