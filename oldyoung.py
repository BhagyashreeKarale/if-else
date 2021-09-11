age1=int(input("Enter first person's age:\n"))
age2=int(input("Enter second person's age:\n"))
age3=int(input("Enter third person's age:\n"))
if age1>age2 and age1>age3:
    if age2<age1 and age2<age3:
        print("First person is the older and second one is eldest among three")
    elif age3<age1 and age3<age2:
        print("First person is oldest and third one is eldest among three")
elif age2>age1 and age2>age3:
    if age1<age2 and age1<age3:
        print("Second person is the oldest and first person is eldest among three")
    elif age3<age1 and age3<age2:
        print("Second person is oldest and third one is eldest among three")
elif age3>age1 and age3>age2:
    if age1<age2 and age1<age3:
        print("Third person is oldest and first person is eldest among three")
    else:
        print("Third person is oldest and second person is eldest among three")