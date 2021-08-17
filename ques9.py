# Question 9
# Consider the following rules:
# People 5 years and above in age can go to school.
# People 18 years and above in age can vote in elections.
# People 21 years and above in age can drive a car.
# People 24 years and above in age can marry.
# People 25 years and above in age can legally drink.

# Create a flowchart that takes the age of the user as input. 
# Print what all activities the user can do from the list above. 
# For example, if user enters age as 20, the code should print:
# You can go to school
# You can vote in elections

# If user enters age as 24, the code will print:
# You can go to school
# You can vote in elections
# You can drive a car
# You can marry
# Submit the flowchart as well as the code.

age=int(input("Enter your age:\n"))
if age>=5:
    if age>=18:
        if age>=21:
            if age>=24:
                if age>=25:
                    print("You can go to school\nYou can vote in elections\nYou can drive a car\nYou can marry\nyou can drink legally")
                else:
                    print("You can go to school\nYou can vote in elections\nYou can drive a car\nYou can marry")
            else:
                print("You can go to school\nYou can vote in elections\nYou can drive a car")
        else:
            print("You can go to school\nYou can vote in elections")
    else:
        print("You can go to school")
else:
    print("Come back when you grow up child!")
