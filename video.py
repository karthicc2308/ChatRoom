from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import filedialog

def encrypt_file(file_path, key):
    with open(file_path, 'rb') as file:
        file_data = file.read()

    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(file_data)

    encrypted_file_path = file_path.replace('.', '_encrypted.')
    with open(encrypted_file_path, 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)

    return encrypted_file_path

def decrypt_file(encrypted_file_path, key):
    with open(encrypted_file_path, 'rb') as encrypted_file:
        encrypted_data = encrypted_file.read()

    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data)

    decrypted_file_path = encrypted_file_path.replace('_encrypted.', '_decrypted.')
    with open(decrypted_file_path, 'wb') as decrypted_file:
        decrypted_file.write(decrypted_data)

    return decrypted_file_path

# Generate a key (store this securely for decryption)
key = Fernet.generate_key()

# Create a Tkinter root window (it won't be shown)
root = tk.Tk()
root.withdraw()

# Ask the user to select a video file
video_path = filedialog.askopenfilename(title="Select a Video", filetypes=[("Video files", "*.mp4;*.avi;*.mkv")])

if not video_path:
    print("No video selected. Exiting.")
else:
    # Encrypt the selected video
    encrypted_video_path = encrypt_file(video_path, key)
    print(f"Video encrypted and saved to: {encrypted_video_path}")

    # Decrypt the video
    decrypted_video_path = decrypt_file(encrypted_video_path, key)
    print(f"Video decrypted and saved to: {decrypted_video_path}")