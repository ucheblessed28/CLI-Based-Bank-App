# Import the required functions from other files
from createAccount import createAccount
from accountList import accountList
from update import updateAccount
from transfer import transfer
from kycFalse import kycFalse
from addNew import addNewField
from previewAccount import previewAccount
from deleteAccount import deleteAccount

def bank():
    while True:
        print("=" * 50)
        print("|             Welcome to Cloud Bank             |")
        print("=" * 50)
        print("_" * 50, "\n")
        print("|             Please Choose An Operation         |")
        print("_" * 50, "\n")
        print("| 1. |  Create an Account                        |") # createAccount.py
        print("_" * 50, "\n")
        print("| 2. |  View All Existing Accounts               |") # accountList.py
        print("_" * 50, "\n")
        print("| 3. |  Update An Account                        |") # update.py
        print("_" * 50, "\n")
        print("| 4. |  Make A Transfer                          |") # transfer.py
        print("_" * 50, "\n")
        print("| 5. |  Check KYC Status                         |") # kycFalse.py
        print("_" * 50, "\n")
        print("| 6. |  Update Accounts Database                 |") # addNew.py
        print("_" * 50, "\n")
        print("| 7. |  Delete An Account                        |") # deleteAccount.py
        print("_" * 50, "\n")
        print("| 8. |  Preview Account Details                  |")  # New option to preview account
        print("_" * 50, "\n")
        print("| 9. |  Exit Application                         |") # exit
        print("_" * 50, "\n")

        # Ask the user to select an option
        try:
            choice = int(input("Please enter the number of your choice: "))
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 8.")
            continue # Return to the menu if input is invalid

        if choice == 1:
            createAccount()  # Call the function to create a new account
            print("Account creation completed successfully.")
            break  # Exit the loop after successful account creation

        elif choice == 2:
            accountList()  # Call the function to view all accounts
            print("Displaying all accounts completed successfully.")
            break  # Exit the loop after successfully displaying all accounts

        elif choice == 3:
            updateAccount()  # Call the function to update account details
            print("Account update completed successfully.")
            break  # Exit the loop after successfully updating the account

        elif choice == 4:
            transfer()  # Call the function to make a transfer
            print("Transfer completed successfully.")
            break  # Exit the loop after successful transfer

        elif choice == 5:
            kycFalse()  # Call the function to print accounts with KYC False
            print("KYC check completed successfully.")
            break  # Exit the loop after successfully checking KYC

        elif choice == 6:
            addNewField()  # Call the function to add a new field to all accounts
            print("Field addition to all accounts completed successfully.")
            break  # Exit the loop after successfully adding the field

        elif choice == 7:
            deleteAccount()  # Call the function to delete an account
            print("Account deletion completed successfully.")
            break  # Exit the loop after successfully deleting the account

        elif choice == 8:
            previewAccount()
            print("Account preview completed successfully.")
            break  # Exit the loop after successfully previewing the account

        elif choice == 9:
            print("Thank you for using Nectra Bank. Goodbye!")
            break  # Exit the loop and terminate the program
        else:
            print("Invalid choice! Please enter a number between 1 and 8.")
            continue  # If the choice is invalid, show the menu again

if __name__ == "__main__":
    bank()