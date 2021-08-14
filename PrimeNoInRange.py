#Find prime no within in range

def ChkPrime(iStart,iEnd):
    primeList=[]
    while iStart != iEnd :
        for iCnt in range(2,iStart) :
                if iStart % iCnt == 0: 
                    break

        else:
           primeList.append(iStart)
           
        iStart +=1
        
    return primeList

def main():
    pList=[]
    print("Enter the range")
    iStart=int(input())
    iEnd=int(input())
    
    pList=ChkPrime(iStart,iEnd)
    print("Prime numbers within range are:")
    print(pList)

if __name__=="__main__":
    main()