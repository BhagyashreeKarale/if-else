num1=int(input("Enter 1st value:\n"))
num2=int(input("Enter 2nd value:\n"))
operator=(input("Enter operator for your operation:\n"))
if operator==("+"):
    print("Result of your addition is",num1+num2)
elif operator==("-"):
    print("Result of your substraction is",num1-num2)
elif operator==("*"):
    print("Result of your multiplication is",num1*num2)
elif operator==("*"):
    print("Result of your division is",num1/num2)
elif operator==("/"):
    print("Result of your floor division is",num1//num2)
elif operator==("//"):
    print("Remainder of your division is",num1%num2)
elif operator==("**"):
    print(num1,"raised to",num2,"is",num1**num2)
else:
    print("Please enter a valid operator or number")
    