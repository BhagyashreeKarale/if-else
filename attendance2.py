total_clases=int(input("Enter the total number of classes held:\n"))
attended_classes=int(input("Enter the total number of classes attended:\n"))
per_total=(75*total_clases)/100
per_stu=(attended_classes*100)/total_clases
if per_stu<per_total:
    print("Your attendance is",per_stu,"%")
    print("You aren't allowed to sit for the examination")
else:
    print("Your attendance is",per_stu,"%")
    print("You are allowed to sit for the examination")