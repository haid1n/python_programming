# Imported modules
from Crypto.Cipher import AES

from Crypto.Random import get_random_bytes

import os


# Decrypt file
def decrypt_file(file_name, key):
    # Read the encrypted file data
    with open(file_name, 'rb') as file:
        encrypted_data = file.read()
    
    # Extract the IV from the beginning of the encrypted data
    iv = encrypted_data[:16]
    
    # Create AES cipher object
    cipher = AES.new(key, AES.MODE_CFB, iv)
    
    # Decrypt the file data
    decrypted_data = cipher.decrypt(encrypted_data[16:])
    
    # Write the decrypted data to a new file
    with open(file_name[:-4], 'wb') as file:
        file.write(decrypted_data)
    
    print(f"File '{file_name}' decrypted successfully!")

# Example usage
key = get_random_bytes(16)  # AES key must be either 16, 24, or 32 bytes long

decrypt_file('file_io/image_copy.jpg.enc', key)