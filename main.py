import pyAesCrypt


# ask user for master key, then use master key to decrypt password file
master_key = input('Enter master key: ')
print(f'master key: {master_key}')

# give password or enter password
give_or_enter = input('(a)give me password || (d)take password: ')
print(f'user wants to: {give_or_enter}')

# TODO: Need to encrypt and decrypt file(https://pypi.org/project/pyAesCrypt/)
# TODO: If passwd.txt does not exist, create and encrypt file

if give_or_enter == 'a':
    d = {}
    # convert passwd.txt data into a dictionary
    with open('passwd.txt', 'r') as passwd:
        for line in passwd:
           (key, val) = line.split()
           d[key] = val
        print(d)

# ask user for account name, then search the dict with the key(account name) and return the value(password)
elif give_or_enter == 'd':
    with open('passwd.txt', 'a') as passwd:
        passwd.writelines('four there\n')

else:
    print('wrong! try again bozo')
