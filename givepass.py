#!/usr/bin/env python
import pyAesCrypt
import os
import sys


# ask user for master key. Used to Encrypt and decrypt passwd.txt.aes file
master_key = input('Enter master key: ')

# run the program until user choose to quit
while True:

    # delete temp.txt file since the file is only used while reading and writing to file
    def delete_temp_file():
        try:
            if os.path.exists('temp.txt'):
              os.remove('temp.txt')

        except:
            print('Error found in delete_temp_file()')

    def create_file(key):
        try:
            with open('temp.txt', 'a') as passwd:
                # encrypt file
                pyAesCrypt.encryptFile("temp.txt", "passwd.txt.aes", master_key)

                delete_temp_file()
        except:
            print('Error found in create_file()')

    def check_master_key(key):
        try:
            pyAesCrypt.decryptFile("passwd.txt.aes", "temp.txt", master_key)
            pyAesCrypt.encryptFile("temp.txt", "passwd.txt.aes", master_key)
            delete_temp_file()
        except:
            print('WRONG! Try again bozo')
            delete_temp_file()

    # checks if passwd.txt.aes file exist, else we need to create a new one
    try:
        if os.path.exists('passwd.txt.aes'):
            check_master_key(master_key)
        else:
            create_file(master_key)
    except:
        print('Error found while checking if passwd.txt.aes file exist')

    # Options presented to user
    options = input('(R)Read Credentials - (W)Write Credentials - (D)Display All Accounts - (Q)Quit - (!)Hard Reset: ').capitalize()

    def check_input_valid(input):
        try:
            if type(input) == str and len(input) > 0:
                return True
            else:
                print('Invalid Input')
                delete_temp_file()
        except:
            print('Error found in check_input_valid')
            delete_temp_file()

    def read_passwd(key, account):

        try:
            passwords = {}

            check_input_valid(account)
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

            # look for the account password in passwd file data
            password = passwords[account]
            return password
        except:
            print('Error found in read_passwd()')

    def write_passwd(key, account, username, password):

        try:
            check_input_valid(account)
            check_input_valid(username)
            check_input_valid(password)

            # check that account does not exist already
            accounts = read_all_accounts(key)
            if accounts != None:
                for i in accounts:
                    print(i)
                    if i == account:
                        print('Account with that name already exist! Please enter a different account')

            # decrypt file
            pyAesCrypt.decryptFile("passwd.txt.aes", "temp.txt", master_key)

            with open('temp.txt', 'a') as passwd:
                passwd.writelines(f'{account} {username} {password}\n')

            # encrypt file
            pyAesCrypt.encryptFile("temp.txt", "passwd.txt.aes", master_key)
            delete_temp_file()

        except:
            print('Error found in write_passwd()')

    def read_all_accounts(key):

        try:
            passwords = {}

            # decrypt file
            pyAesCrypt.decryptFile("passwd.txt.aes", "temp.txt", master_key)

            # convert passwd.txt.aes data into a dictionary
            with open('temp.txt', 'r') as passwd:
                for line in passwd:
                   (key, val1, val2) = line.split()
                   passwords[key] = f'USERNAME: {val1}  PASSWORD: {val2}'

            # encrypt file
            pyAesCrypt.encryptFile("temp.txt", "passwd.txt.aes", master_key)
            delete_temp_file()

            print('All Your Accounts:')
            for key in passwords.keys():
                if key != None:
                    print(key)

        except:
            print('Error found in read_all_accounts()')

    def hard_reset():
        try:
            confirmed = input('This Action Will ERASE All Your Data! Do you want to continue? [Y/N]: ').capitalize()

            if confirmed == 'Y':
                os.remove('passwd.txt.aes')
                print('Hard reset executed')
                delete_temp_file()
            else:
                print('Hard Reset Not Confirmed')
                delete_temp_file()
        except:
            print('Error found in hard_reset()')

    # if passwd file does not exist, create one
    try:
        with open('passwd.txt.aes', 'r') as passwd:
            print('passwd.txt.aes file found')
    except:
        print('creating passwd file')
        create_file(master_key)

    # read file
    if options == 'R':
        account = input('Enter account name: ')

        print(read_passwd(master_key, account))

    # write(append) to file
    elif options == 'W':
        account = input('Enter account name: ')

        username = input('Enter username or email for account: ')

        password = input('Enter password: ')

        write_passwd(master_key, account, username, password)
        print('Account saved')

    elif options == 'D':
        read_all_accounts(master_key)

    elif options == 'Q':
        print('Quitting program...')
        sys.exit()

    elif options == '!':
        hard_reset()

    else:
        print('You entered a invalid option')

    # Read entire passwd.txt.aes document. Used for debugging
    def read_encrypted_file(key):

        try:
            # decrypt file
            pyAesCrypt.decryptFile("passwd.txt.aes", "temp.txt", master_key)

            with open('temp.txt', 'r') as passwd:
                print('read_encrypted_file() reading tempt.txt:')
                print(passwd.read())

            # encrypt file
            pyAesCrypt.encryptFile("temp.txt", "passwd.txt.aes", master_key)

            delete_temp_file()
        except:
            print('Error found in read_encrypted_file()')

    # read_encrypted_file(master_key)
