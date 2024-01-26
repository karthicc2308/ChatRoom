from cryptography.fernet import Fernet

# Generate a key
key = Fernet.generate_key()

# Create a Fernet object with the key
cipher_suite = Fernet(key)

# Get user input for the plaintext message
plaintext_message = input("Enter the message to encrypt: ").encode()

# Encrypt user input
ciphertext = cipher_suite.encrypt(plaintext_message)

# Decrypt the ciphertext to verify
decrypted_text = cipher_suite.decrypt(ciphertext)

print("Key:", key.decode())
print("Ciphertext:", ciphertext.decode())
print("Decrypted message:", decrypted_text.decode())