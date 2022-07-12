import pyAesCrypt


# ask user for master key, then use master key to decrypt password file
master_key = input('Enter master key: ')
print(f'master key: {master_key}')

# give password or enter password
give_or_take = input('(a)give me password || (d)take password: ')
print(f'user wants to: {give_or_take}')

# TODO: Need to encrypt and decrypt file(https://pypi.org/project/pyAesCrypt/)
# TODO: If passwd.txt does not exist, create and encrypt file

def create_file(key):
    with open('passwd.txt', 'a') as passwd:
        # encrypt file
        pyAesCrypt.encryptFile("passwd.txt", "passwd.txt.aes", master_key)
        print(f'passwd encrypted: {passwd}')

# if passwd file does not exist create one
try:
    with open('passwd.txt', 'r') as passwd:
        print('passwd file found')
except:
    print('creating passwd file')
    create_file(master_key)

# if give_or_take == 'a':
#     d = {}
#     # convert passwd.txt data into a dictionary
#     with open('passwd.txt', 'r') as passwd:
#         for line in passwd:
#            (key, val) = line.split()
#            d[key] = val
#         print(d)
#
#     # # decrypt file
#     # pyAesCrypt.decryptFile("passwd.txt.aes", "passwd.txt", master_key)
#     #
#     # # encrypt file
#     # pyAesCrypt.encryptFile("passwd.txt", "passwd.txt.aes", master_key)
#
# # ask user for account name, then search the dict with the key(account name) and return the value(password)
# elif give_or_take == 'd':
#     with open('passwd.txt', 'a') as passwd:
#         passwd.writelines('four there\n')
#
# else:
#     print('wrong! try again bozo')
