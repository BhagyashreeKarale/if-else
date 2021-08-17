salary=int(input("enter your salary"))
yos=int(input("enter number of years of service"))
if yos>5:
	print("you'll get bonus of",(5*salary)/100)
else:
	print("you have to work for",5-yos,"more yoss to get bonus")