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

def read_passwd(key):
    d = {}

    # decrypt file
    pyAesCrypt.decryptFile("passwd.txt.aes", "temp.txt", master_key)

    # convert passwd.txt data into a dictionary
    with open('temp.txt', 'r') as passwd:
        for line in passwd:
           (key, val) = line.split()
           d[key] = val
        print(f'here are your passwords: {d}')

    # encrypt file
    pyAesCrypt.encryptFile("temp.txt", "passwd.txt.aes", master_key)

    delete_temp_file()

# if passwd file does not exist create one
try:
    with open('passwd.txt.aes', 'r') as passwd:
        print('passwd file found')
except:
    print('creating passwd file')
    create_file(master_key)

# read file
if give_or_take == 'a':
    read_passwd(master_key)

# write(append) to file
elif give_or_take == 'd':

    # decrypt file
    pyAesCrypt.decryptFile("passwd.txt.aes", "temp.txt", master_key)

    with open('temp.txt', 'a') as passwd:
        passwd.writelines('three there\n')

    # encrypt file
    pyAesCrypt.encryptFile("temp.txt", "passwd.txt.aes", master_key)

    delete_temp_file()

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

read_encrypted_file(master_key)
