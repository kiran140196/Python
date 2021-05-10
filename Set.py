#You can treat set as dictionary without value

def main():
	arr={10,20.5,"Hello",10}

	print(type(arr))
	print(arr)

	#arr[0]=50; set is not mutlable
	#print(arr)

	print(len(arr))

	for value in arr:
		print(value)

	if "Hello" in arr:
		print("Hello is there")

	arr.add(20)
	print(arr)

	arr.remove(20)
	print(arr)

	arr.discard(20.5)
	print(arr)
 
	#arr.remove(120) if we pass the value to remove which is not in set then it will give key error
	#print(arr)

	arr.discard(120) #if we pass the value to discard which is not in set then it will ignore and won't give any error
	print(arr)

	#arr.pop() don't use pop in set bcoz pop remove last element but set contain unorder data and you don't know the last element so don't use pop in set
	#print(arr)

if __name__=="__main__":
	main()