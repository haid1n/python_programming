# Imported modules
from Crypto.Cipher import AES

from Crypto.Random import get_random_bytes

import os


# Encrypt files
def encrypt_file(file_name, key):
    # Generate a random initialization vector (IV)
    iv = get_random_bytes(16)
    
    # Create AES cipher object
    cipher = AES.new(key, AES.MODE_CFB, iv)
    
    # Read the file data
    with open(file_name, 'rb') as file:
        file_data = file.read()
    
    # Encrypt the file data
    encrypted_data = iv + cipher.encrypt(file_data)
    
    # Write the encrypted data to a new file
    with open(file_name + '.enc', 'wb') as file:
        file.write(encrypted_data)
    
    print(f"File '{file_name}' encrypted successfully!")

# Example usage
key = get_random_bytes(16)  # AES key must be either 16, 24, or 32 bytes long

encrypt_file('file_io/image_copy.jpg', key)
