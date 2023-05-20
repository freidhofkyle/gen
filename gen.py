################################################################################
# Programn: gen.py
# Description: Generates random passwords and saves them to a file.
#
# Creator: Kyle Freidhof
# Email: freidhofkyle@gmail.com
# Created Date: 2023-05-19
#
# License: GPL3 License
# License URL: https://www.gnu.org/licenses/gpl-3.0.en.html


#
# This script generates random passwords based on user-defined length and saves them
# to a file. It provides options to encrypt the credentials and supports decryption
# to retrieve the saved credentials. The script uses the cryptography library and
# requires Python 3.6+.
#
# Dependencies: cryptography
# Prerequisites: Python 3.6+
#
# Usage: python password_generator.py [-u USERNAME] [-l LENGTH] -f FILENAME [-e] [-d]
################################################################################


import random
import string
import argparse
from cryptography.fernet import Fernet

def generate_password(length):
     # Generate a random password with the specified length
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def save_credentials(username, password, filename, encrypt=False):
    # Save the username and password to a file
    with open(filename, 'w') as file:
        if encrypt:
            # Generate an encryption key and create a cipher suite
            key = Fernet.generate_key()
            cipher_suite = Fernet(key)
            encrypted_username = cipher_suite.encrypt(username.encode())
            encrypted_password = cipher_suite.encrypt(password.encode())
            file.write(encrypted_username.decode() + '\n')
            file.write(encrypted_password.decode())
            print("Encrypted credentials saved to", filename)
            print("Encryption Key:", key.decode())
        else:
            file.write(username + '\n')
            file.write(password)
            print("Credentials saved to", filename)

def load_encrypted_credentials(filename, key):
     # Load and decrypt the username and password from a file
    with open(filename, 'r') as file:
        encrypted_username = file.readline().strip()
        encrypted_password = file.read()
        cipher_suite = Fernet(key)
        decrypted_username = cipher_suite.decrypt(encrypted_username.encode())
        decrypted_password = cipher_suite.decrypt(encrypted_password.encode())
        return decrypted_username.decode(), decrypted_password.decode()

# Create an ArgumentParser object to handle command-line arguments

parser = argparse.ArgumentParser(description="Password Generator")
# Add command-line arguments using add_argument() method
# '-u' or '--username': specifies the username (optional)
# 'type=str': the value will be a string
# 'help': provides a description of the argument

parser.add_argument('-u', '--username', type=str, help="Username")
# '-l' or '--length': specifies the length of the password (optional)
# 'type=int': the value will be an integer
# 'help': provides a description of the argument``
parser.add_argument('-l', '--length', type=int, help="Length of the password")

# '-f' or '--filename': specifies the filename to save or load the credentials (required)
# 'type=str': the value will be a string
# 'required=True': this argument must be provided
# 'help': provides a description of the argument
parser.add_argument('-f', '--filename', type=str, required=True, help="Filename to save or load the credentials")

# '-e' or '--encrypt': specifies the encryption flag (optional)
# 'action='store_true'': this argument doesn't require a value, only the presence of the flag
# 'help': provides a description of the argument

parser.add_argument('-e', '--encrypt', action='store_true', help="Encrypt the credentials file")

# '-d' or '--decrypt': specifies the decryption flag (optional)
# 'action='store_true'': this argument doesn't require a value, only the presence of the flag
# 'help': provides a description of the argument
parser.add_argument('-d', '--decrypt', action='store_true', help="Decrypt the credentials file")
# Parse the command-line arguments and store them in the 'args' variable
args = parser.parse_args()

if args.encrypt and args.decrypt:
    print("Error: Cannot encrypt and decrypt simultaneously. Please choose either -e or -d.")
    exit(1)

if args.encrypt:
    # Generate a password and save the encrypted credentials
    password = generate_password(args.length)
    print("Generated Password:", password)
    save_credentials(args.username, password, args.filename, args.encrypt)

if args.decrypt:
    # Prompt for the encryption key and decrypt the credentials
    key = input("Enter the encryption key: ")
    decrypted_username, decrypted_password = load_encrypted_credentials(args.filename, key)
    print("Decrypted Username:", decrypted_username)
    print("Decrypted Password:", decrypted_password)

#print("Generated Password:", password)

#save_password(password, args.filename, args.encrypt)


































