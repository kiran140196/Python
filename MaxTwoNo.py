#Maximum of two numbers

def Maximum(iNo1,iNo2):
    if iNo1 > iNo2:
        return iNo1
    else:
        return iNo2

def main():
    print("Enter first no")
    iNo1=int(input())
    print("Enter second no")
    iNo2=int(input())
    
    iRes=Maximum(iNo1,iNo1)
    print("Maximum no from {} and {} is {}".format(iNo1,iNo2,iRes))


    #OR
    iRes=max(iNo1,iNo2)
    print("Maximum no from {} and {} is {}".format(iNo1,iNo2,iRes))

   
if __name__=="__main__":
    main()