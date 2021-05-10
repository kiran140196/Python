def main():
	name=input("Enter the file name that you want to read")
	fobj=open(name,"r")	
	size=int(input("Enter number of charachters to read"))
	print("Data from the file is")
	print(fobj.read(size))

if __name__=="__main__":
	main()