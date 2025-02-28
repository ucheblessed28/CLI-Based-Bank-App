# Import the accounts dictionary from accounts.py
from accounts import accounts
import pprint

def addNewField():
    global accounts

    # Step 1: Ask for the new field name (e.g., phone number)
    newKey = input("Enter the new key to add (e.g., 'phoneNumber'): ")

    # Step 2: Add the new key to all accounts with an empty value
    for accountNumber, account in accounts.items():
        account[newKey] = ""  # Set the initial value to an empty string

    # Step 3: Save the updated accounts to the accounts.py file
    with open('accounts.py', 'w') as f:
        f.write("accounts = ")
        pprint.pprint(accounts, stream=f, width=100, indent=4)

    print(f"New field '{newKey}' has been added to all accounts with an empty value.")

# Run the addNewField function
if __name__ == "__main__":
    addNewField()






# # Import the accounts dictionary from accounts.py
# from accounts import accounts
# import pprint

# def addNewField():
#     global accounts

#     # Step 1: Ask for the account number to update
#     while True:
#         try:
#             accountNumber = input("Enter the account number to update: ")

#             # Check if the account number is 10 digits
#             if accountNumber.isdigit() and len(accountNumber) == 10:
#                 if accountNumber in accounts:
#                     print(f"Account details: {accounts[accountNumber]}")

#                     # Step 2: Ask the user for the new field name (e.g., phone number)
#                     new_key = input("Enter the new key to add (e.g., 'phoneNumber'): ")

#                     # Step 3: Ask for the value of the new key (e.g., phone number value)
#                     new_value = input(f"Enter the value for the new field '{new_key}': ")

#                     # Step 4: Add the new key-value pair to the account details
#                     accounts[accountNumber][new_key] = new_value

#                     # Step 5: Save the updated accounts to the accounts.py file
#                     with open('accounts.py', 'w') as f:
#                         f.write("accounts = ")
#                         pprint.pprint(accounts, stream=f, width=100, indent=4)

#                     print(f"New field '{new_key}' has been added to account {accountNumber} successfully.")
#                     break
#                 else:
#                     print("Account not found!")
#                     break
#             else:
#                 print("Invalid account number format. Must be a 10-digit number.")
#         except ValueError:
#             print("Invalid input! Account number should be a number.")

# # Run the addNewField function
# if __name__ == "__main__":
#     addNewField()
