# Import the required functions from other files
from createAccount import createAccount
from accountList import accountList
from update import updateAccount
from transfer import transfer
from kycFalse import kycFalse
from addNew import addNewField
from deleteAccount import deleteAccount

# Main bank function that displays the menu
def bank():
    while True:  # Loop for repeated menu display
        # Display the main menu
        print("=" * 50)
        print("|             Welcome to Nectra Bank             |")
        print("=" * 50)
        print("_" * 50, "\n")
        print("|             Please Choose An Operation         |")
        print("_" * 50, "\n")
        print("| 1. |  Create an Account                        |")  # createAccount.py
        print("_" * 50, "\n")
        print("| 2. |  View All Existing Accounts               |")  # accountList.py
        print("_" * 50, "\n")
        print("| 3. |  Update An Account                        |")  # update.py
        print("_" * 50, "\n")
        print("| 4. |  Make A Transfer                          |")  # transfer.py
        print("_" * 50, "\n")
        print("| 5. |  Check KYC Status                         |")  # kycFalse.py
        print("_" * 50, "\n")
        print("| 6. |  Update Accounts Database                 |")  # addNew.py
        print("_" * 50, "\n")
        print("| 7. |  Delete An Account                        |")  # deleteAccount.py
        print("_" * 50, "\n")
        print("| 8. |  Exit Application                         |")  # exit
        print("_" * 50, "\n")

        # Ask the user to select an option
        try:
            choice = int(input("Please enter the number of your choice: "))
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 8.")
            continue  # Prompt user again if input is invalid

        # Call the corresponding function based on user's choice
        if choice == 1:
            createAccount()  # Call the function to create a new account
        elif choice == 2:
            accountList()  # Call the function to view all accounts
        elif choice == 3:
            updateAccount()  # Call the function to update account details
        elif choice == 4:
            transfer()  # Call the function to make a transfer
        elif choice == 5:
            kycFalse()  # Call the function to print accounts with KYC False
        elif choice == 6:
            addNewField()  # Call the function to add a new field to all accounts
        elif choice == 7:
            deleteAccount()  # Call the function to delete an account
        elif choice == 8:
            print("Thank you for using Nectra Bank. Goodbye!")
            break  # Exit the loop and terminate the program
        else:
            print("Invalid choice! Please enter a number between 1 and 8.")

# Only run this if the file is executed directly
if __name__ == "__main__":
    bank()
