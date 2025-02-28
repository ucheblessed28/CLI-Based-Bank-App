from accounts import accounts

def previewAccount():
    # Prompt the user to enter the account number
    try:
        accountNumber = int(input("Enter Account Number to Preview: "))
    except ValueError:
        print("Invalid input! Please enter a valid account number.")
        return
    
    # Check if the account number exists in the accounts dictionary
    if str(accountNumber) in accounts:
        account = accounts[str(accountNumber)]
        # Display account details
        print("\nAccount Details:")
        print("=" * 50)
        print(f"\nAccount Name: {account['accountName']}")
        print(f"Account Number: {account['accountNumber']}")
        print(f"Account Balance: ${account['accountBalance']}")
        print(f"Phone Number: {account['phoneNumber']}")
        print(f"Email Address: {account['email']}")
        print(f"KYC Status: {'Completed' if account['KYC'] else 'Not Completed'} \n")
        print("=" * 50, "\n")
    else:
        print("Account number not found!")

# To test the function, you can call previewAccount() directly if you want.
if __name__ == "__main__":
    previewAccount()
