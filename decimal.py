num=float(input("Enter a number:\n"))
wnum=num*10
if wnum % 5 == 0:
    print(num)
elif wnum % 10 > 5 :
    print(int(num)+1)
else:
    print(int(num)-1)