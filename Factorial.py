#Factioral of number

def Fact(iNo):
    iFact=1
    while(iNo!=1):
        iFact=iFact*iNo
        iNo-=1
        
    return iFact

def main():
    iNo=int(input("Enter the no of which factorial you want"))
    iRes=Fact(iNo)
    
    print("Factioral of {} is {}".format(iNo,iRes))

if __name__=="__main__":
    main()