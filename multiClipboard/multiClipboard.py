###
# Target Release:       1.0
# Code Status:          Complete
# Code Developer:       Sourav
# Script Name:          multiClipboard.py
# How to run:           python multiClipboard.py <command>
###

import sys          # To access arguments
import clipboard    # To access clipboard functions
import json         # To work with JSON files

# MANUAL OVERRIDE: Access whatever is stored currently on your clipboard
# data = clipboard.paste()
# print(data)

# MANUAL OVERRIDE: Write anything to the clipboard
# clipboard.copy('ANYTHING')

# MANUAL OVERRIDE: Access the command-line arguments (incl. script name)
# print(sys.argv)

# MANUAL OVERRIDE: Access the command-line arguments (excl. script name)
# print(sys.argv[1:])

# Define a JSON file which will store our clipboard data. This is because: JSON is similar to Python dictionaries.
SAVED_DATA = "clipboard.json"

# Defining a script that will save data in a JSON file at a location of your choice. This JSON file will act as your clipboard storage.
def save_items(filepath, data):         
    with open(filepath, "w") as f:      # Opening a file in 'write' mode. Create one; otherwise override.
        json.dump(data, f)              # Dump the data into the file we opened

# MANUAL OVERRIDE: Function call to write data to clipboard storage to a file where we want to store data.
# save_items("/////test.json", {"key":"value"})

# Defining a function to read everything that we have stored in our clipboard storage file.
def load_items(filepath):
    try:
        with open(filepath, "r") as f:      # If the file exists, open the file in the 'read' mode.
            data = json.load(f)
            return data
    except:
        return {}       # Error handling: Try to open the file. Otherwise return the empty dictionary.

# Start with checking the number of arguments
if len(sys.argv) == 2:      # 2 because: scriptname is 1st, the other one is the command
    command = sys.argv[1]
    data = load_items(SAVED_DATA)       # Keeping our clipboard file ready
    # Checking which argument you entered
    if command == 'save':               
        print(f'You entered this command: ',command)
        key = input('Enter a key: ')    # The key at which the data will be stored
        data[key] = clipboard.paste()   # Your clipboard data will be assigned to the key you saved above
        save_items(SAVED_DATA, data)    # Saving the data into the JSON file that we defined at the beginning
        print(f'SUCCESS! Your clipboard data is stored with this key: ',key)
    elif command == 'load':
        print(f'You entered this command: ',command)
        key = input('Enter a key: ')    # The key at which the data was stored
        if key in data:
            clipboard.copy(data[key])
            print(f'SUCCESS! The data associated with this key is added to your clipboard')
        else:
            print("ERROR! This key doesn't exists!")
    elif command == 'list':
        print(f'You entered this command: ',command)
        print(data)
    elif command == 'help':
        print(f'You entered this command: ',command)
        print(f'\nThis script helps you maintain a clipboard-as-a-file. \n\nValid commands:')
        print(f'> help: Describe the script.')
        print(f'> save: Save something to the clipboard file.')
        print(f'> load: Load something specific that is saved in the clipboard file.')
        print(f'> list: List everything that is saved to the clipboard file.')
    else:
        print(f'Unknown command!')      # For commands which are not valid
else:
    print(f'This command accepts only 1 command at a time.')