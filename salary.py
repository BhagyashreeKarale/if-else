salary=int(input("Enter your salary:\n"))
yos=int(input("Enter number of years of service:\n"))
if yos>5:
	print("You'll get bonus of",(5*salary)/100)
else:
	print("You have to work for",5-yos,"more years to get bonus")