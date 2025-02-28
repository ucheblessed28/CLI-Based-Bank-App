# Cloud Bank Admin System

Cloud Bank is a simple Python-based banking application that allows admins to create and manage accounts, perform transfers, update account details, and more. This application simulates a basic banking system with features like account creation, transfer of funds, viewing account details, and handling KYC (Know Your Customer) status.

## Features

- **Create an Account**: Allows users to create a new account with a randomly generated 10-digit account number, a name, balance, and an email address. The KYC status is set to "Not Completed" by default.
- **View Accounts**: Users can view all existing accounts and their details, including KYC status.
- **Update Account**: Users can update various account details such as account name, balance, KYC status, phone number, and email address.
- **Transfer Funds**: Users can make transfers between accounts. Transfer limits are based on the KYC status.
- **Delete Accounts**: Users can delete an account or clear all accounts, after confirming the deletion.
- **Email Validation**: Ensures the correct format for email addresses during account creation using regular expressions (regex).
- **Preview Account**: Users can preview the details of any account by entering its account number.

## Installation

1. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/ucheblessed28/cli-based-bank-app.git
    ```
2. Navigate to the project directory:
    ```bash
    cd /cli-based-bank-app
    ```

3. Ensure Python 3.8+ is installed on your machine.

## Usage

1. Run the main application (`bank.py`) to interact with the banking system:
    ```bash
    python bank.py
    ```

2. Follow the on-screen prompts to choose from the available operations like creating an account, viewing account details, transferring funds, etc.

## File Structure

- **accounts.py**: Contains a dictionary of all accounts.
- **bank.py**: Main application that presents the menu and calls appropriate functions.
- **createAccount.py**: Handles the creation of new accounts.
- **update.py**: Allows updating account details.
- **transfer.py**: Manages fund transfers between accounts.
- **deleteAccount.py**: Provides functionality to delete an account or clear all accounts.
- **kycFalse.py**: Lists accounts with incomplete KYC status.
- **addNew.py**: Adds new fields to accounts.
- **accountList.py**: Displays the list of all accounts.

## Contributions

Contributions are welcome! Feel free to submit issues, suggest new features, or contribute to the code.

## License

This project is open-source and available under the MIT License.

---