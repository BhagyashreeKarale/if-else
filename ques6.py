# Question 6
# Draw a flowchart for this question and write the program.
# Take two numbers as input from the user in variables varx and vary.
# Check whether varx is divisible by vary.
# If yes, print Divisible else print Not Divisible.
varx=int(input("Enter dividend:\n"))
vary=int(input("Enter divisor:\n"))
if varx % vary == 0:
    print(varx,"is completely divisible by",vary)
else:
    print(varx,"isn't completely divisible by",vary)
