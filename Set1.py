def main():
	arr={10,20,30,40}

	print(type(arr))

	temp=list(arr) #list here is class name
	print(type(temp))
	temp[1]=21
	arr=set(temp)	#set here is class name
	print(arr)

if __name__=="__main__":
	main()