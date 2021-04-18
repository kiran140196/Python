def Addition(LIST):
	iCnt=0
	sum=0
	for iCnt in range(len(LIST)):
		sum=sum+LIST[iCnt]
	return sum

def main():
	Arr=[10,20,30,40]
	
	sum=Addition(Arr)
	print("Addition is:",sum)

if __name__=="__main__":
	main()