import pyAesCrypt
import os

# ask user for master key, then use master key to decrypt password file
master_key = input('Enter master key: ')
print(f'master key: {master_key}')

# give password or enter password
give_or_take = input('(a)give me password || (d)take password: ')
print(f'user wants to: {give_or_take}')

# TODO: Need to encrypt and decrypt file(https://pypi.org/project/pyAesCrypt/)

def create_file(key):
    with open('passwd.txt', 'a') as passwd:
        # encrypt file
        pyAesCrypt.encryptFile("passwd.txt", "passwd.txt.aes", master_key)
        print(f'encrypted passwd created: {passwd}')

    # delete passwd.txt file since the file is a temp file
    if os.path.exists("passwd.txt"):
      os.remove("passwd.txt")
      print('passwd.txt removed')
    else:
      print("The file does not exist")

# if passwd file does not exist create one
try:
    with open('passwd.txt', 'r') as passwd:
        print('passwd file found')
except:
    print('creating passwd file')
    create_file(master_key)

# # read file
# if give_or_take == 'a':
#     d = {}
#
#     # decrypt file
#     pyAesCrypt.decryptFile("passwd.txt.aes", "passwd.txt", master_key)
#
#     # convert passwd.txt data into a dictionary
#     with open('passwd.txt', 'r') as passwd:
#         for line in passwd:
#            (key, val) = line.split()
#            d[key] = val
#         print(d)
#
#     # encrypt file
#     pyAesCrypt.encryptFile("passwd.txt", "passwd.txt.aes", master_key)
#
# # write(append) to file
# elif give_or_take == 'd':
#
#     # decrypt file
#     pyAesCrypt.decryptFile("passwd.txt.aes", "passwd.txt", master_key)
#
#     with open('passwd.txt', 'a') as passwd:
#         passwd.writelines('four there\n')
#
#     # encrypt file
#     pyAesCrypt.encryptFile("passwd.txt", "passwd.txt.aes", master_key)
#
# else:
#     print('wrong! try again bozo')
#
# def read_encrypted_file(key):
#     print('inside read_encrypted_file()')
#
#     # decrypt file
#     pyAesCrypt.decryptFile("passwd.txt.aes", "passwd.txt", master_key)
