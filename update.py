# Import the accounts dictionary from accounts.py
from accounts import accounts
import pprint

def updateAccount():
    global accounts

    # Step 1: Ask for the account number to update
    while True:
        try:
            accountNumber = input("Enter the account number to update: ")

            # Check if the account number is 10 digits
            if accountNumber.isdigit() and len(accountNumber) == 10:
                if accountNumber in accounts:
                    print(f"Account details: {accounts[accountNumber]}")
                    
                    # Step 2: Ask the user which detail to update
                    print("\nWhich detail would you like to update?")
                    print("1. Account Name")
                    print("2. Account Balance")
                    print("3. KYC Status")
                    print("4. Phone Number")
                    print("5. Email Address")
                    
                    # Input the detail to update
                    choice = input("Enter the number of the detail to update (1, 2, 3, 4, 5): ")

                    if choice == '1':
                        # Update Account Name
                        newName = input("Enter the new Account Name: ")
                        accounts[accountNumber]["accountName"] = newName
                    elif choice == '2':
                        # Update Account Balance
                        while True:
                            try:
                                newBalance = float(input("Enter Deposit Amount: "))
                                accounts[accountNumber]["accountBalance"] += newBalance # Add to existing balance
                                break
                            except ValueError:
                                print("Invalid input! Please enter a valid number for the balance.")
                    elif choice == '3':
                        # Update KYC Status
                        while True:
                            kycStatus = input("Enter the new KYC Status (yes/no): ").lower()
                            if kycStatus in ['yes', 'no']:
                                accounts[accountNumber]["KYC"] = True if kycStatus == 'yes' else False
                                break
                            else:
                                print("Invalid input! Please enter 'yes' or 'no'.")
                    elif choice == '4':
                        # Update Phone Number
                        newPhone = input("Enter the new Phone Number: ")
                        accounts[accountNumber]["phoneNumber"] = newPhone
                    elif choice == '5':
                        # Update Email Address
                        email = input("Enter the new Email Address: ")
                        accounts[accountNumber]["email"] = email
                    else:
                        print("Invalid choice. Please select an option.")
                        continue
                    
                    # Step 3: Save the updated accounts to the accounts.py file
                    with open('accounts.py', 'w') as f:
                        f.write("accounts = ")
                        pprint.pprint(accounts, stream=f, width=100, indent=4)

                    print(f"Account {accountNumber} has been updated successfully.")
                    break
                else:
                    print("Account not found!")
                    break
            else:
                print("Invalid account number format. Must be a 10-digit number.")
        except ValueError:
            print("Invalid input! Account number should be a number.")

# Run the updateAccount function
if __name__ == "__main__":
    updateAccount()