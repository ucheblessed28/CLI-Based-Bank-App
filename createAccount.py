from accounts import accounts
import json
import pprint
import random
import re  # Importing the regular expression module

def createAccount():
    global accounts

    accountName = input("Enter Account Name: ")
    phoneNumber = input("Enter Phone Number: ")
    
    # Step 5: Validate Email using Regex
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    while True:
        email = input("Enter Email Address: ")
        if re.match(email_regex, email):
            break  # If email is valid, break the loop
        else:
            print("Invalid email format! Please enter a valid email address.")



    # Generate an account number
    while True:
        accountNumber = str(random.randint(0000000000, 9999999999))  # Random 10-digit number
        if accountNumber not in accounts:
            break
    print(f"Account Created! \nAccount Number: {accountNumber}")

    # Input for deposit balance (Let's assume the user opens the account with a deposit balance)

    while True:
        try:
            accountBalance = float(input("Enter Deposit Balance: "))
            if accountBalance >= 1000:
                break
            else:
                print("Low Balance! Deposit balance must be 1000 and above!")
        except ValueError:
            print("Invalid Balance! Please enter a valid number")
    
    # Input for KYC status
    while True:
        kyc = input("Has KYC been completed? (yes/no): ").lower()
        if kyc in ["yes", "no"]:
            kyc = True if kyc == "yes" else False
            break
        else:
            print("Invalid input! Please enter 'yes' or 'no'.")

    # Add the new account to the database
    accounts[accountNumber] = {
        "accountName": accountName,
        "accountNumber": accountNumber,
        "accountBalance": accountBalance,
        "KYC": kyc,
        "phoneNumber": phoneNumber,
        "email": email
    }

    print(f"Account created successfully! Account number: {accountNumber}")
    print(f"Account Holder: {accountName}, \nAccount Balance: {accountBalance} \nKYC: {'Completed' if kyc else 'Not Completed'}")

    # Update the accounts file

    # Save the updated accounts dictionary back to the accounts.py file with pretty-printing
    with open("accounts.py", "w") as f:
        f.write("accounts = ")
        # Manually write the dictionary in Python format (ensuring booleans stay True/False)
        pprint.pprint(accounts, stream = f, width = 100, indent = 4)

# Call the createAccount Function
if __name__ == "__main__":
    createAccount()