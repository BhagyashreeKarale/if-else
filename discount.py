unit=int(input("Enter quantity of units:\n"))
price=unit*100
if price==1000 or price>1000:#here instead of using or,i can join both the conditions and put it as "if price>=1000:"
    print("You'll get a discount of RS",(price*10)/100)
else:
    print(r"Buy items worth 1000 or more to get 10,'%',discount")#r indicates the raw string 
                                                             #i have used it to print the percentage symbol(%)
                                                             #without it python would have recognized % as modulus
#or else if i dont want to use r i.e. the raw string i can simply use:
# print("buy items worth 1000 or more to get 10",'%',"discount")