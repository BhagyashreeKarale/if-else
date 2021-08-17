unit=int(input("enter quantity of units"))
price=unit*100
if price==1000 or price>1000:
    print("you'll get a discount of RS",(price*10)/100)
else:
    print(r"buy items worth 1000 or more to get 10%discount")

