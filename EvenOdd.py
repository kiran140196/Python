def EvenOdd(Value):
	if Value % 2==0:
		return True
	else:
		return False

def main():
	print("Enter no")
	value=int(input())
	
	if EvenOdd(value):
		print("No is even")
	else:
		print("No is odd")

if __name__=="__main__":
	main()