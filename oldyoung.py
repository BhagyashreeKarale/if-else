age1=int(input("enter first person's age"))
age2=int(input("enter second person's age"))
age3=int(input("enter third person's age"))
if age1>age2 and age1>age3:
    if age2<age1 and age2<age3:
        print("first person is the older and second one is eldest among three")
    elif age3<age1 and age3<age2:
        print("first person is oldest and third one is eldest among three")
elif age2>age1 and age2>age3:
    if age1<age2 and age1<age3:
        print("second person is the oldest and first person is eldest among three")
    elif age3<age1 and age3<age2:
        print("second person is oldest and third one is eldest among three")
elif age3>age1 and age3>age2:
    if age1<age2 and age1<age3:
        print("third person is oldest and first person is eldest among three")
    else:
        print("third person is oldest and second person is eldest among three")