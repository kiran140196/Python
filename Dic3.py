def main():
	flag=False
	batches={"PPA":12500,"LB":11000,"Python":13000,"Angular":10000,"LSP":11000}	
	print("Enter the batch name")
	name=input()

	#print(batches.get(name,"There is no such batch"))
	for value in batches: 	#instead of using this much for loop used above method
		if name== value:
			print(batches.get(name))
			flag=True
	if flag==False:
		print("There is no such batch")


if __name__=="__main__":
	main()