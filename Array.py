from array import *


def main():
	arr=array('i',[11,21,51,101,111])
	print(type(arr))

	print(len(arr))

	print(arr[0])
	
	print("Using for loop")
	for i in range(len(arr)):
		print(arr[i])
	
	print("using directly like arr")
	print(arr)

	print("Using for each like in java")
	for no in arr:
		print(no)

	iCnt=0
	print("Using while loop")
	while iCnt < len(arr):
		print(arr[iCnt])
		iCnt+=1

if __name__=="__main__":
	main()