import threading

Amount=1000

def ATM(func,kulup):
	print("Inside ATM")
	func(kulup)

def Deposit(kulup):
	kulup.acquire()
	print("Inside Deposit")
	iValue=int(input("Enter the amount to deposit"))
	global Amount
	Amount=Amount+iValue
	print("Deposit successful - Balance is:",Amount)
	kulup.release()

def Withdraw(kulup):
	kulup.acquire()
	print("Inside Withdraw")
	iValue=int(input("Enter the amount to withdraw"))
	global Amount
	if iValue > Amount:
		print("There is no sufficient balance")
	else:
		Amount=Amount-iValue
		print("Withdraw successful - Balance is:",Amount)
	kulup.release()

def main():
	print("Inside main")

	kulup=threading.Lock()

	t1=threading.Thread(target=ATM, args=(Deposit,kulup,))
	t2=threading.Thread(target=ATM, args=(Withdraw,kulup,))

	t1.start()
	t2.start()

	t1.join()
	t2.join()

	print("ATM application closed")

if __name__=="__main__":
	main()