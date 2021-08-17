num1=int(input("enter 1st value"))
num2=int(input("enter 2nd value"))
operator=(input("enter operator for num2our operation"))
if operator==("+"):
    print("result of num2our addition is",num1+num2)
elif operator==("-"):
    print("result of num2our substraction is",num1-num2)
elif operator==("*"):
    print("result of num2our multiplication is",num1*num2)
elif operator==("*"):
    print("result of num2our division is",num1/num2)
elif operator==("/"):
    print("result of num2our floor division is",num1//num2)
elif operator==("//"):
    print("remainder of num2our division is",num1%num2)
elif operator==("**"):
    print(num1,"raised to",num2,"is",num1**num2)
else:
    print("please enter a valid operator or number")
    