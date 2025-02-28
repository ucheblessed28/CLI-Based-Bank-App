# Import the accounts dictionary from accounts.py
from accounts import accounts
import pprint

def deleteAccount():
    global accounts

    # Step 1: Ask for the account number to delete
    while True:
        try:
            accountNumber = input("Enter the account number to delete: ")

            # Check if the account number is 10 digits
            if accountNumber.isdigit() and len(accountNumber) == 10:
                if accountNumber in accounts:
                    print(f"Account details: {accounts[accountNumber]}")
                    
                    # Step 2: Confirm the deletion
                    confirm = input(f"Are you sure you want to delete the account {accountNumber}? (yes/no): ").lower()
                    if confirm == 'yes':
                        # Step 3: Delete the account
                        del accounts[accountNumber]
                        
                        # Step 4: Save the updated accounts to the accounts.py file
                        with open('accounts.py', 'w') as f:
                            f.write("accounts = ")
                            pprint.pprint(accounts, stream=f, width=100, indent=4)

                        print(f"Account {accountNumber} has been deleted successfully.")
                        break
                    else:
                        print("Account deletion cancelled.")
                        break
                else:
                    print("Account not found!")
                    break
            else:
                print("Invalid account number format. Must be a 10-digit number.")
        except ValueError:
            print("Invalid input! Account number should be a number.")

# Run the deleteAccount function
if __name__ == "__main__":
    deleteAccount()
