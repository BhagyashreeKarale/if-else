id = "bhagyashreekarale07"
password = "bk17"
welcome_msg = input ("Welcome to PYTHON\nDo you have an account?(Yes/No):\n")
if welcome_msg == "yes":
    login_msg = input ("Are you ready for login:\n")
    if login_msg == "yes":
            user_id = input ("Please enter your ID:\n")
            if user_id == id:
                    user_password = input ("Enter password:\n")
            else:
                    print ("Please enter a valid ID:\n")
            if user_password == password:
                     print ("Login successful")
            else:
                print ("Incorrect password")
    else:
        print ("Get back when you are ready for login.\nHope to see you ASAP!")
else:
    sign_up = input ("Are you ready for signup?\n")
    if sign_up == "yes":
        name = input ("Enter your name\n")
        gmail = input ("Enter your mail id\n")
        contact = input ("Enter your contact number\n")
        idname = input ("What id name would you prefer?\n")
        new_pass = input ("Create password") 
        confirm_pass = input ("Re-enter your password:\n")
        if new_pass == confirm_pass:
            print ("Congratulations!Your account has been created successfully.")
            print ("Your ID is",idname)
            print ("Your password is",new_pass)
        else:
            print ("Confirmed password didn't matched the password created")
    else:
        print ("Get back when you are ready for sign-up.\nHope to see you ASAP!")