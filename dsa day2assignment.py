mobile = input("Enter mobile number: ")

if mobile.isdigit():  
    if len(mobile) == 10:  
        if mobile[0] == '6' or mobile[0] == '7' or mobile[0] == '8' or mobile[0] == '9':
            print("Valid Indian Mobile Number")
        else:
            print("Invalid: Should start with 6, 7, 8, or 9")
   