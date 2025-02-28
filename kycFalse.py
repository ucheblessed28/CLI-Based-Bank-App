# Import the accounts dictionary from accounts.py
from accounts import accounts

def kycFalse():
    print("Accounts with KYC status False:\n")
    
    # Flag to check if any accounts are found
    found = False

    # Step 1: Loop through all accounts
    for accountNumber, account in accounts.items():
        # Step 2: Check if KYC is False
        if not account.get("KYC", False):
            found = True
            # Step 3: Print account details where KYC is False
            print(f"Account Name: {account['accountName']}")
            print(f"Account Number: {account['accountNumber']}")
            print(f"Account Balance: {account['accountBalance']}")
            print(f"KYC Status: {'Completed' if account['KYC'] else 'Not Completed'}")
            print("-" * 40)

    # Step 4: If no accounts are found with KYC False
    if not found:
        print("No accounts with KYC status set to False.")

# Run the kycFalse function
if __name__ == "__main__":
    kycFalse()
