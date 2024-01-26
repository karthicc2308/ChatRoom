from cryptography.fernet import Fernet

# Generate a key
key = Fernet.generate_key()

# Create a Fernet object with the key
cipher_suite = Fernet(key)

# Get user input for the plaintext message
def encrypt(txt):
    plaintext_message = cipher_suite.encrypt(toBinary(txt))

# Encrypt user input
    ciphertext = cipher_suite.encrypt(plaintext_message)
    return ciphertext
# Decrypt the ciphertext to verify
def decrypt(txt):   
    decrypted_text = cipher_suite.decrypt(txt)
    return decrypted_text
# print("Key:", key.decode())
# print("Ciphertext:", ciphertext.decode())
# print("Decrypted message:", decrypted_text.decode())