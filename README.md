
# GIVEPASS

GIVEPASS is a Python script for storing dummy account credentials. The script can be run from the command line. Credentials are stored in an external file(passwd.txt.aes) encrypted with AES256-CBC [pyAesCrypt](https://pypi.org/project/pyAesCrypt/)

**DON'T USE THIS TO STORE REAL CREDENTIALS! THIS SCRIPT WAS NOT DESIGNED AS A SECURE WAY TO STORE CREDENTIALS!**

## Installation for Linux

Download GIVEPASS folder:
```bash
git clone https://github.com/borelli28/givepass.git
```

Navigate to directory where givepass.py is located:
```bash
cd /Home/user/Downloads/givepass/
```

Install required libraries from requirements.txt:
```bash
pip3 install -r requirements.txt
```

Give execute permission to givepass.py file:
```bash
chmod +x givepass.py
```

Run script
```bash
./givepass.py
```

## Usage

```bash

# First prompt ask for a master key.
# This key will be used to encrypt and decrypt(Symmetric) the passwd.txt.aes file where all your credentials are stored
Enter master key:

# You have six options:
(R)Read Credentials - (W)Write Credentials - (A)Display All Accounts - (D)Remove a Credential - (Q)Quit - (!)Hard Reset:

# Read Credentials: Ask you for an account name(Ex: twitter, google, etc.) and it will output the username & password for that account
Enter account name:
# Output:
USERNAME: joe123   PASSWORD: ilovegod

# Write Credentials: Ask for an Account name, an Username, and a Password. This will add a new credential
Enter account name:
Enter username or email for account:
Enter password:
#output:
Account saved

# Display All Accounts: Will retrieve all Account names and display them in the console for you
# Output:
All Your Accounts:
account1
account2
account3

# Remove a Credential: Will remove the given account
Enter the account that you want to remove:

# Hard Reset: Will delete the file(passwd.txt.aes) where credentials are stored. Used to delete all credentials at once
This Action Will ERASE All Your Data! Do you want to continue? [Y/N]:

```

## TO DO

- Add log for read_passwd() & read_all_accounts() when an account is not found
- Add test cases
