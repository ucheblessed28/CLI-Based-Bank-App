from accounts import accounts
import pprint

def transfer():
    global accounts

    # Input for the sender's account number
    while True:
        try:
            senderAccount = input("Enter Sender's Account Number: ")
            if senderAccount.isdigit() and len(senderAccount) == 10:
                if senderAccount in accounts:
                    print(f"Sender's Account Details: {accounts[senderAccount]}")
                    break
                else:
                    print("Account not found! Please enter a valid account number.")
            else:
                print("Invalid account number! Must be a 10-digit number.")
        except ValueError:
            print("Invalid Input! Please type a numerical value")

    # Input for the receiver's account number
    while True:
        try:
            receiverAccount = input("Enter Receiver's Account Number: ")
            if receiverAccount.isdigit() and len(receiverAccount) == 10:
                if receiverAccount in accounts:
                    print(f"Receiver's Account Details: {accounts[receiverAccount]}")
                    break
                else:
                    print("Account not found! Please enter a valid account number.")
            else:
                print("Invalid account number! Must be a 10-digit number.")
        except ValueError:
            print("Invalid Input! Please type a numerical value")

    # Input for the amount to transfer
    while True:
        try:
            amount = float(input("Enter Amount to Transfer: "))
            if amount >= 1000:
                senderKyc = accounts[senderAccount]['KYC']
                maxTransfer = 5000 if not senderKyc else float('inf')

                # Check if transfer exceeds the maximum transfer limit
                if amount > maxTransfer:
                    print(f"Transfer limit exceeded! Maximum transfer limit is ${maxTransfer}.")
                elif amount > accounts[senderAccount]['accountBalance']:
                    print("Insufficient funds! Please enter a valid amount.")
                else:
                    # Proceed with the transfer
                    accounts[senderAccount]['accountBalance'] -= amount
                    accounts[receiverAccount]['accountBalance'] += amount

                    # update the accounts file
                    with open("accounts.py", "w") as f:
                        f.write(f"accounts = ")
                        pprint.pprint(accounts, stream=f, indent=4)

                    print(f"Transfer of ${amount} successful from {accounts[senderAccount]['accountName']} to {accounts[receiverAccount]['accountName']}")

                    print(f"{accounts[senderAccount]['accountNumber']} New Balance: ${accounts[senderAccount]['accountBalance']}")

                    print(f"{accounts[receiverAccount]['accountNumber']} New Balance: ${accounts[receiverAccount]['accountBalance']}")

                    break
            else:
                print("Invalid Amount! Minimum transfer amount is $1000.")
        except ValueError:
            print("Invalid Amount! Please enter a valid number.")

# Call the transfer function
if __name__ == "__main__":
    transfer()