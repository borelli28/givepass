


# ask user for master key, then use master key to decrypt password file
master_key = input('Enter master key: ')
print(f'master key: {master_key}')

# give password or enter password
give_or_enter = input('(a)give me password || (d)take password: ')
print(f'user wants to: {give_or_enter}')
if give_or_enter == 'a':
    passwd = open('passwd.txt', 'r')
    print(passwd.read())

elif give_or_enter == 'd':
    passwd = open('passwd.txt', 'a')
    passwd.writelines('that\n')


# ask user for account name, then search the dict with the key(account name) and return the value(password)
