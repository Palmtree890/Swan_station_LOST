from playsound import playsound
import os
import time

# --- Configuration ---
# You must have both of these files in your folder!
FAILURE_SOUND_FILE = "Countdown.mp3"
SUCCESS_SOUND_FILE = "Success_Reset.mp3" 

# Get the full, robust paths
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
MP3_FAILURE_PATH = os.path.join(SCRIPT_DIR, FAILURE_SOUND_FILE)
MP3_SUCCESS_PATH = os.path.join(SCRIPT_DIR, SUCCESS_SOUND_FILE)
# ---------------------

print("Welcome to the Swan Station Interface.")
print("Enter the sequence of numbers to prevent a system failure.")

while True:
    numbers = input(">: ").strip()
    
    if numbers == "4 8 15 16 23 42":
        print("\nSequence accepted. System reset.")
        # Play the success sound ONLY when numbers are correct
        playsound(MP3_SUCCESS_PATH, False) 
        print("Restarting countdown...\ndisabling Lockdown for 108 minutes.\n")
        # Give the success sound time to play before the next prompt starts
        time.sleep(3) 
    else:
        print("\n" + ("SYSTEM FAILURE " * 8 + "\n") * 5)
        # Play the failure sound ONLY when numbers are incorrect
        playsound(MP3_FAILURE_PATH, False) 
        print("Incorrect input. Please try again immediately.")

# This script was inspired by the TV show Lost
# It simulates the input of the infamous numbers at the Swan Station
