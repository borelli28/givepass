#!/usr/bin/env python
import pyAesCrypt
import os
import sys

# run the program until user choose to quit
while True:

    # ask user for master key. Used to Encrypt and decrypt passwd.txt.aes file
    master_key = input('Enter master key: ')

    # delete temp.txt file since the file is only used while reading and writing to file
    def delete_temp_file():
        try:
            if os.path.exists('temp.txt'):
              os.remove('temp.txt')

        except:
            print('Error found in delete_temp_file()')

    def create_file():
        try:
            with open('temp.txt', 'a') as passwd:
                # encrypt file
                pyAesCrypt.encryptFile("temp.txt", "passwd.txt.aes", master_key)

                delete_temp_file()
        except:
            print('Error found in create_file()')

    def key_correct():
        try:
            pyAesCrypt.decryptFile("passwd.txt.aes", "temp.txt", master_key)
            pyAesCrypt.encryptFile("temp.txt", "passwd.txt.aes", master_key)
            delete_temp_file()
            return True
        except:
            delete_temp_file()

    def passwd_exist():
        try:
            if os.path.exists('passwd.txt.aes'):
                return True
            else:
                return False
        except:
            print('Error found in check_passwd()')

    def check_input_valid(input):
        try:
            if type(input) == str and len(input) > 0:
                return True
            else:
                print('Invalid Input \n')
                delete_temp_file()
        except:
            print('Error found in check_input_valid')
            delete_temp_file()

    def read_passwd(account):
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

    def write_passwd(account, username, password):
        try:
            duplicate = False
            check_input_valid(account)
            check_input_valid(username)
            check_input_valid(password)

            # decrypt file
            pyAesCrypt.decryptFile("passwd.txt.aes", "temp.txt", master_key)

            # check that account does we don't have an account with the same name already
            accounts = {}
            with open('temp.txt', 'r') as passwd:
                for line in passwd:
                   (key, val1, val2) = line.split()
                   accounts[key] = f'USERNAME: {val1}  PASSWORD: {val2} \n'
                if len(accounts) > 0:
                    for i in accounts:
                        if i == account:
                            print('Account with that name already exist! Please enter a different account \n')
                            duplicate = True
            if not duplicate:
                with open('temp.txt', 'a') as passwd:
                    passwd.writelines(f'{account} {username} {password}\n')
                    print('New account saved \n')

            # encrypt file
            pyAesCrypt.encryptFile("temp.txt", "passwd.txt.aes", master_key)
            delete_temp_file()

        except:
            print('Error found in write_passwd()')

    def read_all_accounts():
        try:
            passwords = {}

            # decrypt file
            pyAesCrypt.decryptFile("passwd.txt.aes", "temp.txt", master_key)

            # convert passwd.txt.aes data into a dictionary
            with open('temp.txt', 'r') as passwd:
                for line in passwd:
                   (key, val1, val2) = line.split()
                   passwords[key] = f'USERNAME: {val1}  PASSWORD: {val2} \n'

            # encrypt file
            pyAesCrypt.encryptFile("temp.txt", "passwd.txt.aes", master_key)
            delete_temp_file()

            print('All Your Accounts:')
            for i in passwords.keys():
                if i != None:
                    print(f'- {i} \n')

        except:
            print('Error found in read_all_accounts()')

    # remove a single credential
    def remove_cred(account):
        try:
            # decrypt file
            pyAesCrypt.decryptFile("passwd.txt.aes", "temp.txt", master_key)

            # iterate through the file until you find the account
            lines = None
            accounts = {}
            with open('temp.txt', 'r') as passwd:
                lines = passwd.readlines()

            with open('temp.txt', 'r') as passwd:
                # convert passwd.txt data into a dictionary
                for line in passwd:
                    (key, val, val2) = line.split()
                    accounts[key] = f'{val} {val2}'

            try:
                # get credential line from dictionary
                values = accounts[account]
                cred = f'{account} {values}'

                with open('temp.txt', 'w') as passwd:
                    for line in lines:
                        if line.strip('\n') != cred:
                            passwd.write(line)
                    print(f'{account} removed')
            except:
                print('Account you entered does not exist \n')

            # encrypt file
            pyAesCrypt.encryptFile("temp.txt", "passwd.txt.aes", master_key)
            delete_temp_file()
        except:
            print('Error found in remove_cred()')

    def hard_reset():
        confirmed = input('This Action Will ERASE All Your Data! Do you want to continue? [Y/N]: ').capitalize()

        if confirmed == 'Y':
            os.remove('passwd.txt.aes')
            print('Hard reset executed \n')
            quit_program()
        else:
            print('Hard Reset Aborted \n')

    def quit_program():
        print('Quitting... \n')
        '''
        Don't call exit() in a try-except block
        exit() raise an exception named SystemExit which will break your program
        '''
        sys.exit()

    # Options presented to user
    def show_options():
        options = input('(R)Read Credentials - (W)Write Credentials - (A)Display All Accounts - (D)Remove a Credential - (Q)Quit - (!)Hard Reset: ').capitalize()
        print('\n')

        # read file
        if options == 'R':
            account = input('Enter account name: ')
            print(read_passwd(account))
            show_options()

        # write(append) to file
        elif options == 'W':
            account = input('Enter account name: ')
            username = input('Enter username or email for account: ')
            password = input('Enter password: ')
            write_passwd(account, username, password)
            show_options()

        elif options == 'A':
            read_all_accounts()
            show_options()

        elif options == 'D':
            account = input('Enter the account that you want to remove: ')
            remove_cred(account)
            show_options()

        elif options == 'Q':
            quit_program()

        elif options == '!':
            hard_reset()
            # Executed if hard reset is aborted
            show_options()

        else:
            print('You entered a invalid option \n')
            show_options()

    # Read entire passwd.txt.aes document. Used for debugging
    # def read_encrypted_file(key):
    #
    #     try:
    #         # decrypt file
    #         pyAesCrypt.decryptFile("passwd.txt.aes", "temp.txt", master_key)
    #
    #         with open('temp.txt', 'r') as passwd:
    #             print('read_encrypted_file() reading tempt.txt:')
    #             print(passwd.read())
    #
    #         # encrypt file
    #         pyAesCrypt.encryptFile("temp.txt", "passwd.txt.aes", master_key)
    #
    #         delete_temp_file()
    #     except:
    #         print('Error found in read_encrypted_file()')
    # read_encrypted_file(master_key)

    # Check that master key is correct and then show options prompt
    if key_correct():
        if passwd_exist():
            show_options()
        else:
            create_file()
    # If this gets executed it means that the user is creating a new DB(passwd file)
    elif not key_correct() and not passwd_exist():
        create_file()
        if passwd_exist():
            show_options()
