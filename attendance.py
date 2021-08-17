a=int(input("enter the total number of classes held"))
b=int(input("enter the total number of classes attended"))
e=(input("If you have health issues enter 'Y' and if you don't have enter 'N'"))
c=(75*a)/100
d=(b*100)/a
if d<c:
    if e=="n":
        print("Your attendance is",d,"%")
        print("You aren't allowed to sit for the examination")
    else:
        print("Your attendance is",d,"%")
        print("You are allowed to sit for the examination even with low attendance because of health issues")
else:
    print("Your attendance is",d,"%")
    print("You are allowed to sit for the examination")