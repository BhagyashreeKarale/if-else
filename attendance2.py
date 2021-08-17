total_clases=int(input("enter the total number of classes held"))
attended_classes=int(input("enter the total number of classes attended"))
per_total=(75*total_clases)/100
per_stu=(attended_classes*100)/total_clases
if per_stu<per_total:
    print("your attendance is",per_stu,"%")
    print("you aren't allowed to sit for the examination")
else:
    print("your attendance is",per_stu,"%")
    print("you are allowed to sit for the examination")