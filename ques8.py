# Question 8
# Create a flowchart that takes a number as user input. 
# Check if this number is divisible by 5 and 15 both.
# Hint: You will need to use nested if-else for this question.
# Submit flowchart as well as code.
num=int(input("Enter a number"))
if num % 5 == 0:
    if num % 15 == 0:
        print(num,"is divisible by both 5 and 15")
    else:
        print(num,"is divisible only by 5")
else:
    print(num,"is divisible by neither 5 nor 15")
