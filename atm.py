pin = 2395
balance = 60000
max_amount = balance-250
print("Welcome to BANK OF MAHARASHTRA")
card=input("Please insert your card.When inserted type 'done'.\n")
if card == "done":
    pin_input = int(input ("Enter your PIN\n"))
    if pin_input == pin:
        print ("1.Withdraw")
        print ("2.Balance Enquiry")
        option = int (input ("Enter your option number of your process\n") )
        if option == 1:
            amount = int(input ("Enter amount of cash withdrawal\nShould be in round figure(MIN=500 and MAX=10000)\n"))
            if amount>balance:
                    print ("Insufficient balance.")
            elif amount == balance:
                max = (input ("Minimum balance of 250.0 is required.\nPlease enter amount less than or equal to",max_amount) )
                account_type = int(input ("1.Savings Account\n2.Current Account\n3.Credit\nPLease enter option number of your account type") )
                print ("Your transaction is completed.\nPlease collect your cash and card")
            else:#amount<balance:
                account_type = (input ("1.Savings Account\n2.Current Account\n3.Credit\nPLease enter number of your account type") )
                print ("Your transaction is completed.\nPlease collect your cash and card")
        else:
            print ("Your Balace is",balance)
    else:#if pin is not 2395#in this case
            print ("INCORRECT PIN")
else:
    print ("Please enter the card to proceed the transaction")
            

                
                    
                
