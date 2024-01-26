from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import filedialog

# Generate a key (store this securely for decryption)
key = Fernet.generate_key()

# Create a Tkinter root window (it won't be shown)
root = tk.Tk()
root.withdraw()

# Ask the user to select an image file
image_path = filedialog.askopenfilename(title="Select an Image", filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])

if not image_path:
    print("No image selected. Exiting.")
else:
    # Encrypt the selected image
    with open(image_path, "rb") as image_file:
        image_data = image_file.read()

    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(image_data)

    with open("encrypted_image.bin", "wb") as encrypted_file:
        encrypted_file.write(encrypted_data)

    # Decrypt the image
    with open("encrypted_image.bin", "rb") as encrypted_file:
        encrypted_data = encrypted_file.read()

    fernet = Fernet(key)  # Use the same key for decryption
    decrypted_data = fernet.decrypt(encrypted_data)

    # Save the decrypted data to an image file
    with open("decrypted_image.jpg", "wb") as decrypted_file:
        decrypted_file.write(decrypted_data)

    print("Image encryption and decryption completed.")
