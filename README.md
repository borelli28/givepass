# GIVEPASS

GIVEPASS is a Python script for storing dummy account credentials. The script can be executed from the command line. Credentials are stored in an external file(passwd.txt.aes) encrypted with AES256 with [pyAesCrypt](https://pypi.org/project/pyAesCrypt/)

**DON'T USE THIS TO STORE REAL CREDENTIALS! THIS SCRIPT IS NOT A SECURE WAY TO STORE YOUR CREDENTIALS!**

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install foobar
```

## Usage

```python
# First prompt ask for a master key.
# This key will be used to encrypt and decrypt(Symmetric) the passwd.txt.aes file where all your credentials are stored
Enter master key:

# You have four options:
(R)Read Credentials - (W)Write Credentials - (D)Display All Accounts - (!)Hard Reset:

# Read Credentials: Ask you for an account name(Ex: twitter, google, etc.) and it will output the username & password for that account
Enter account name:
# Output:
USERNAME: joe123   PASSWORD: ilovegod

# Write Credentials: Ask for an Account name, an Username, and a Password. This will add a new credential
# Display All Accounts: Will retrieve all Accounts names and display them in the console for you
# Hard Reset: Will delete the file(passwd.txt.aes) where credentials are stored. Used to delete all credentials at once

```

## TODO

- Add option to delete a single credential
- Add print statement in read_passwd() for when an account is not found
