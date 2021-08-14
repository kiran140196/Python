#Ascii value program

def main():
    print("Enter the letter whose ascii value you want")
    key=input()
    print("Ascii value of {} is {}".format(key,ord(key)))

if __name__=="__main__":
    main()