from accounts import accounts

def accountList():
    print("ACCOUNTS LIST:- \n")
    for account in accounts.values():
        print(f"Account Name: {account['accountName']} \nAccount Number: {account['accountNumber']}\nKYC Status: {'Completed' if account['KYC'] else 'Not Completed'} \nAccount Balance: ${account['accountBalance']} \nPhone Number: {account['phoneNumber']} \nEmail Address: {account['email']}\n")

# Call the accountList Function
if __name__ == "__main__":
    accountList()