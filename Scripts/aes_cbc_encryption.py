# Before running this script, install following library
# pip install cryptography

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from base64 import b64encode, b64decode
from os import urandom

def pad(data):
    # PKCS7 padding
    block_size = 16
    padding_length = block_size - len(data) % block_size
    return data + bytes([padding_length] * padding_length)

def unpad(data):
    # PKCS7 unpadding
    padding_length = data[-1]
    return data[:-padding_length]

def encrypt(plaintext, key):
    # Generate a random Initialization Vector (IV)
    iv = urandom(16)
    # Create AES cipher object in CBC mode
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    # Apply padding to plaintext and encrypt
    cipertext = encryptor.update(pad(plaintext)) + encryptor.finalize()
    return iv + cipertext

def decrypt(cipertext, key):
    # Extract IV from the ciphertext
    iv = cipertext[:16]
    cipertext = cipertext[16:]
    # Create AES cipher object in CBC mode
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    # Decrypt and remove padding
    plaintext = unpad(decryptor.update(cipertext) + decryptor.finalize())
    return plaintext

# Example usage
key = urandom(32) # 256-bit key
plaintext = input("Enter the text to be encrypted: ")
bytes_plaintext = plaintext.encode('utf-8')
print('Plaintext: ', plaintext)

# Encrypt the message
encrypted_data = encrypt(bytes_plaintext, key)
print("Encrypted: ", b64encode(encrypted_data).decode('utf-8'))

# Decrypt the message
decrypted_data = decrypt(encrypted_data, key)
print("Decrypted: ", decrypted_data.decode('utf-8'))