from accounts import accounts
import pprint

def clearAllAccounts():
    # Step 1: Ask for confirmation before deleting all accounts
    print("\nWARNING: This action will delete all accounts permanently!\n")
    
    confirm = input("Are you sure you want to delete all accounts? \n \nType 'DELETE' to confirm: ").lower()

    if confirm == 'delete':
        # Step 2: Clear the accounts dictionary
        global accounts
        accounts = {}

        # Step 3: Overwrite the accounts.py file with an empty dictionary
        with open("accounts.py", "w") as f:
            f.write("accounts = {}\n")

        print("All accounts have been deleted successfully!")
    else:
        print("Account deletion cancelled!")

# To test the function, you can call clearAllAccounts() directly if you want.
if __name__ == "__main__":
    clearAllAccounts()  # This will prompt the user for confirmation and delete the accounts if confirmed