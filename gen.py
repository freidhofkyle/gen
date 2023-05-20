import random
import string
import argparse
from cryptography.fernet import Fernet

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def save_credentials(username, password, filename, encrypt=False):
    with open(filename, 'w') as file:
        if encrypt:
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
    with open(filename, 'r') as file:
        encrypted_username = file.readline().strip()
        encrypted_password = file.read()
        cipher_suite = Fernet(key)
        decrypted_username = cipher_suite.decrypt(encrypted_username.encode())
        decrypted_password = cipher_suite.decrypt(encrypted_password.encode())
        return decrypted_username.decode(), decrypted_password.decode()

parser = argparse.ArgumentParser(description="Password Generator")
parser.add_argument('-u', '--username', type=str, help="Username")
parser.add_argument('-l', '--length', type=int, help="Length of the password")
parser.add_argument('-f', '--filename', type=str, required=True, help="Filename to save or load the credentials")
parser.add_argument('-e', '--encrypt', action='store_true', help="Encrypt the credentials file")
parser.add_argument('-d', '--decrypt', action='store_true', help="Decrypt the credentials file")
args = parser.parse_args()

if args.encrypt and args.decrypt:
    print("Error: Cannot encrypt and decrypt simultaneously. Please choose either -e or -d.")
    exit(1)

if args.encrypt:
    password = generate_password(args.length)
    print("Generated Password:", password)
    save_credentials(args.username, password, args.filename, args.encrypt)

if args.decrypt:
    key = input("Enter the encryption key: ")
    decrypted_username, decrypted_password = load_encrypted_credentials(args.filename, key)
    print("Decrypted Username:", decrypted_username)
    print("Decrypted Password:", decrypted_password)

#print("Generated Password:", password)

#save_password(password, args.filename, args.encrypt)


































