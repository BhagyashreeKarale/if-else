total_classes=int(input("Enter the total number of classes held:\n"))
classes_attended=int(input("Enter the total number of classes attended:\n"))
e=(input("If you have health issues enter 'Y' and if you don't have enter 'N'"))
eligible_attendance=(75*total_classes)/100
student_attendance=(classes_attended*100)/total_classes
if student_attendance<eligible_attendance:
    if e=="n":
        print("Your attendance is",student_attendance,"%")
        print("You aren't allowed to sit for the examination")
    else:
        print("Your attendance is",student_attendance,"%")
        print("You are allowed to sit for the examination even with low attendance because of health issues")
else:
    print("Your attendance is",student_attendance,"%")
    print("You are allowed to sit for the examination")