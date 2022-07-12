import pyAesCrypt
import os
import sys

# ask user for master key, then use master key to decrypt password file
master_key = input('Enter master key: ')
print(f'master key: {master_key}')

def check_master_key(key):
    try:
        # decrypt file
        pyAesCrypt.decryptFile("passwd.txt.aes", "temp.txt", master_key)
    except:
        print('WRONG! Try again bozo')
        sys.exit()

check_master_key(master_key)

# give password or enter password
options = input('(R)Read Password - (W)Write Password - (A)Read All Accounts:  ').capitalize()
print(f'user wants to: {options}')

def create_file(key):
    with open('temp.txt', 'a') as passwd:
        # encrypt file
        pyAesCrypt.encryptFile("temp.txt", "passwd.txt.aes", master_key)
        print(f'encrypted passwd created: {passwd}')

        delete_temp_file()

# delete passwd.txt file since the file is a temp file
def delete_temp_file():
    if os.path.exists("temp.txt"):
      os.remove("temp.txt")
      print('temp.txt removed')
    else:
      print("The file does not exist")

def read_passwd(key, account):
    passwords = {}

    # decrypt file
    pyAesCrypt.decryptFile("passwd.txt.aes", "temp.txt", master_key)

    # convert passwd.txt data into a dictionary
    with open('temp.txt', 'r') as passwd:
        for line in passwd:
           (key, val1, val2) = line.split()
           passwords[key] = f'USERNAME: {val1}  PASSWORD: {val2}'
        print(f'here are all your passwords: {passwords}')

    # encrypt file
    pyAesCrypt.encryptFile("temp.txt", "passwd.txt.aes", master_key)

    delete_temp_file()

    # look for the account password in passwd file data
    password = passwords[account]
    return password

def write_passwd(key, account, username, password):

    # check that account does not exist already
    accounts = read_all_accounts(key)
    for i in accounts:
        print(i)
        if i == account:
            print('Account with that name already exist! Please enter a different account')
            sys.exit()

    # decrypt file
    pyAesCrypt.decryptFile("passwd.txt.aes", "temp.txt", master_key)

    with open('temp.txt', 'a') as passwd:

        passwd.writelines(f'{account} {username} {password}\n')

    # encrypt file
    pyAesCrypt.encryptFile("temp.txt", "passwd.txt.aes", master_key)

    delete_temp_file()

def read_all_accounts(key):
    passwords = {}

    # decrypt file
    pyAesCrypt.decryptFile("passwd.txt.aes", "temp.txt", master_key)

    # convert passwd.txt data into a dictionary
    with open('temp.txt', 'r') as passwd:
        for line in passwd:
           (key, val1, val2) = line.split()
           passwords[key] = f'USERNAME: {val1}  PASSWORD: {val2}'

    # encrypt file
    pyAesCrypt.encryptFile("temp.txt", "passwd.txt.aes", master_key)

    delete_temp_file()

    return passwords.keys()

# if passwd file does not exist create one
try:
    with open('passwd.txt.aes', 'r') as passwd:
        print('passwd file found')
except:
    print('creating passwd file')
    create_file(master_key)

# read file
if options == 'R':

    account = input('Enter account name: ')

    print(read_passwd(master_key, account))

# write(append) to file
elif options == 'W':

    account = input('Enter account name:    ')

    username = input('Enter username or email for account:  ')

    password = input('Enter password:   ')

    write_passwd(master_key, account, username, password)
    print('Account saved')

elif options == 'A':

    print(read_all_accounts(master_key))

else:
    print('wrong! try again bozo')

def read_encrypted_file(key):
    print('inside read_encrypted_file()')

    # decrypt file
    pyAesCrypt.decryptFile("passwd.txt.aes", "temp.txt", master_key)

    with open('temp.txt', 'r') as passwd:
        print('reading tempt.txt:')
        print(passwd.read())

    # encrypt file
    pyAesCrypt.encryptFile("temp.txt", "passwd.txt.aes", master_key)

    delete_temp_file()

# read_encrypted_file(master_key)
