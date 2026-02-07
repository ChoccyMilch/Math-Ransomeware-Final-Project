This is a ransomeware I created as a final project for a Ethical Hacking with Python class. 
#
**WARNING: THIS IS FOR EDUCATIONAL PURPOSES ONLY! I AM NOT RESPONSIBLE FOR ANY MISUSE OR DAMAGE CAUSED USING THIS PROGRAM. Even though this is primitive and basic it can still cause unintended damage or data loss if misused!**
DO NOT USE IF YOU DO NOT KNOW HOW THIS WORKS, OR UNDERSTAND THE POSSIBLE RISKS. ALWAYS RUN USING A VIRTUAL MACHINE.
#
There is no server/client code within this project, at some point I may revisit this to clean it up and try to implement server/client communication in order to better my understanding of these concepts. 
#
#**Abstract**
In this project I have tasked myself in creating a simplistic ransomware program targeted at
machines running Windows 10/11. This program’s objectives are to find a hardcoded directory on the
user’s C: drive titled “test_folder” and all subfolder for the purpose of using AES in CBC mode
128-bit encryption paired with HMAC-SHA256 authentication to encrypt all files. The program
will then prompt the victim to answer a simple randomly generated math problem. The console
continuously asks for user input until the correct answer is provided, which will then trigger the
program to decrypt all encrypted files.
#
#**Problem Statement**
This project is an insight to learn how cyber criminals create ransomware and to better understand
the concepts used within these programs outside of the server logic. I did not create any type of
server or implement client code like is done with real world ransomware. The goal of this project
was to create a humorous program that is more-so akin to a ransom-captcha, but using some of the
primary concepts and ideas used in traditional ransomware.
#
#**Approach**
*HARD REQUIRMENT: disable Windows Defender’s Real Time Protection in settings. For
obvious reasons, it really doesn’t like my program.*

I used PyInstaller to bundle all necessary files into an executable.
The libraries used in my code are the OS, sys, random, playsound3, and cryptography.
The OS library makes it easy to identify and navigate through file paths using its “path” module.
With the “path” module I can check to see if the “test_folder” directory exists within the victims
C: drive, and if it does not exist I use path to create it. I can then use the “path” module to check
for a demo file named “important document.txt” and to create it if it doesn’t exist.
The random library allows me to generate two random integers between 1, and 100 for the math
problem.

The playsound3 library allows me to import the "playsound” module which gives me the ability
to play audio from a sound file when the program runs. And the sys Library is used for its
“hasattr” function to find the sound file after executing the bundled executable created with
PyInstaller.

Then most importantly the cryptography library lets me import the Fernet class to create my
own Fernet object. Fernet is a type of symmetric encryption (meaning it uses a single key to both
encrypt and decrypt) using AES in CBC mode for 128-bit encryption and PKCS7 padding. It also
uses HMAC featuring SHA256 for authentication. By instantiating my own Fernet object, I can
use the “generate_key” method to generate our key if one doesn’t already exist and then use the
standard file handling features included in Python to open a new file, write this new key to it, and
then save it.
#
#**Implementation details**
When the program is executed a Fernet key is created if one does not already exist and the
program will check for the FOLDER_PATH directory. If it doesn’t exist it will create the
“test_folder” folder and then insert a demo text file with the text “krabby patty secret formula”. It
will then enter a for loop that calls the “encrypt_file” function for every file in the root folder (in
this case test_folder) and repeat for every file within every subdirectory. The console will appear
and prompt the victim to answer a randomly generated addition math problem. If the victim
inputs the wrong answer they will be prompted again. Once the correct answer is entered the
program will enter a for loop which called the “decrypt_file” function for every file in the
FOLDER_PATH and for every file in its subdirectories.
#
#**Reflection**
With this project I learned a lot. One issue I faced was that when bundling the python file into an
executable with PyInstaller, my initial sound path wouldn’t be able to be found. This required me
to use the sys library to implement a dynamic file path helper function to find the .mp3 file in the
temporary directory PyInstaller creates when executed.
I also got to learn a lot about symmetric encryption and work with it hands-on via Fernet.


