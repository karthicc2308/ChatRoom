from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import filedialog

def encrypt_audio(input_path, output_path, key):
    # Encrypt the audio file
    with open(input_path, "rb") as audio_file:
        audio_data = audio_file.read()

    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(audio_data)

    # Save the encrypted data to a new file
    with open(output_path, "wb") as encrypted_file:
        encrypted_file.write(encrypted_data)

def decrypt_audio(input_path, output_path, key):
    # Decrypt the encrypted audio file
    with open(input_path, "rb") as encrypted_file:
        encrypted_data = encrypted_file.read()

    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data)

    # Save the decrypted data to a new audio file
    with open(output_path, "wb") as decrypted_file:
        decrypted_file.write(decrypted_data)

# Generate a key (store this securely for decryption)
key = Fernet.generate_key()

# Create a Tkinter root window (it won't be shown)
root = tk.Tk()
root.withdraw()

# Ask the user to select an audio file
audio_path = filedialog.askopenfilename(title="Select an Audio File", filetypes=[("Audio files", "*.mp3;*.wav;*.ogg")])

if not audio_path:
    print("No audio file selected. Exiting.")
else:
    # Encrypt the selected audio file
    encrypted_audio_path = "encrypted_audio.bin"
    encrypt_audio(audio_path, encrypted_audio_path, key)
    print("Audio encryption completed.")

    # Decrypt the encrypted audio file
    decrypted_audio_path = "decrypted_audio.wav"  # Change the extension as needed
    decrypt_audio(encrypted_audio_path, decrypted_audio_path, key)
    print("Audio decryption completed.")