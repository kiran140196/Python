#Addition of two numbers program

def Addition(iNo1,iNo2):
    return iNo1+iNo2

def main():
    print("Enter the first no")
    iValue1=int(input())
    print("Enter the second no")
    iValue2=int(input())
    
    iRes=Addition(iValue1,iValue2)
    print("Addition of {} and {} is {}".format(iValue1,iValue2,iRes))

if __name__=="__main__":
    main()