# Bank System

This is a simple console-based bank system implemented in Python. It allows users to perform various banking operations such as creating an account, logging in, depositing and withdrawing funds, transferring money between accounts, and updating account information.

## Getting Started

### Prerequisites

Before running the program, ensure you have the following installed:

- Python 3.x
- MongoDB

### Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/ghiati/bank-system.git
   ```

2. Install the required Python packages:

   ```bash
   pip install pymongo
   ```

3. Start MongoDB service on your local machine.

4. Run the main program:

   ```bash
   python bank_system.py
   ```

## Project Structure

The project follows the following structure :

```
bank-system/
│
├── bank_system.py           # Main script for running the bank system
├── user.py                  # User class definition
│── BankDatabase.py      # Script for database connection and collections
|── check_users.py       # Just checking the users that exist in our database
│── Insert_user.py       # Script for inserting user data into the database

## Usage

- Follow the on-screen prompts to navigate through the menu options.
- Create an account or log in using existing credentials.
- Perform banking operations such as deposit, withdrawal, transfer, etc.


Thank U 

