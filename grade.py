marks=int(input("enter your marks"))
if marks>80:
    print("You got 'A' grade")
elif marks<=80 and marks>=60:
    print("You got 'B' grade")
elif marks<60 and marks>=50:
    print("You got 'C' grade")
elif marks<50 and marks>=45:
    print("You got 'D' grade")
elif marks<45 and marks>=25:
    print("You got 'E' grade")
else:#less than or equal to 25
    print("You got 'F' grade")