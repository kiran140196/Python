def main():
	Employee={11:{"Name":"Piyush","Age":30},21:{"Name":"Kiran","Age":25},51:{"Name":"Prshant","Age":29}}

	
	for eid,einformation in Employee.items():
		print("Employee id is:",eid)
		for key in einformation:
			print(key,einformation[key])

	#OR

	for eid,einformation in Employee.items():
		print("Employee id is:",eid)
		for ename,eage in einformation.items():
			print(ename,eage)

if __name__=="__main__":
	main()