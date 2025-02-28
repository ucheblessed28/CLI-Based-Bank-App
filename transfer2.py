from accounts import accounts
import pprint

def transfer():
    global accounts

    # Input for the sender's account number
    while True:
        try:
            senderAccount = input("Enter Sender's Account Number: ")
            if senderAccount in accounts:
                break
            else:
                print("Account not found! Please enter a valid account number.")
        except ValueError:
            print("Invalid Input! Please type a numerical value")
    
    # Input for the receiver's account number
    while True:
        try:
            receiverAccount = input("Enter Receiver's Account Number: ")
            if receiverAccount in accounts:
                break
            else:
                print("Account not found! Please enter a valid account number.")
        except ValueError:
            print("Invalid Input! Please type a numerical value")
    
    # Input for the amount to transfer
    while True:
        try:
            amount = float(input("Enter Amount to Transfer: "))
            if amount > 0:
                break
            else:
                print("Invalid Amount! Please enter a valid amount")
        except ValueError:
            print("Invalid Amount! Please enter a valid number")
    
    # Check if the sender has enough balance to transfer
    if accounts[senderAccount]["accountBalance"] >= amount:
        # Deduct the amount from the sender's account
        accounts[senderAccount]["accountBalance"] -= amount
        # Add the amount to the receiver's account
        accounts[receiverAccount]["accountBalance"] += amount
        print(f"Transfer of ${amount} successful from {accounts[senderAccount]['accountName']} to {accounts[receiverAccount]['accountName']}")
        print(f"Sender's Account Balance: ${accounts[senderAccount]['accountBalance']}")
        print(f"Receiver's Account Balance: ${accounts[receiverAccount]['accountBalance']}")
    else:
        print("Insufficient Balance! Transfer failed.")
    
    # Update the accounts file
    # Save the updated accounts dictionary back to the accounts.py file with pretty-printing
    with open("accounts.py", "w") as file:
        file.write("accounts = ")
        pprint.pprint(accounts, file)
        print("Accounts updated successfully!")

# Call the transfer function
transfer()