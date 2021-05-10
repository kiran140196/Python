def main():
	name=input("Enter the file name that you want to read")
	fobj=open(name,"r")	
	
	name2=input("Enter the file name that you want to write")
	fobj2=open(name2,"w")

	print("copying the data")
	fobj2.write(fobj.read())

	fobj2=open(name2,"r")
	print("data in copied file is")
	print(fobj2.read())

if __name__=="__main__":
	main()