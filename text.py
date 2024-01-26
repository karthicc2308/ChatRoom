from cryptography.fernet import Fernet

# Generate a key
key = 'bD4Cilsh3I1I6YFc9-DfyhroWxaM01_8F6ced4IKW3o='
print(key)
# Create a Fernet object with the key
cipher_suite = Fernet(key)

# Get user input for the plaintext message
def encrypt(txt):
    ciphertext = cipher_suite.encrypt(txt)
    return ciphertext
# Decrypt the ciphertext to verify
def decrypt(txt):   
    decrypted_text = cipher_suite.decrypt(txt)
    return decrypted_text
# print("Key:", key.decode())
# print("Ciphertext:", ciphertext.decode())
# print("Decrypted message:", decrypted_text.decode())