import sys
import clipboard
import json

# Access whatever is present on your clipboard
# data = clipboard.paste()
# print(data)

# Write anything to the clipboard
# clipboard.copy('abc')

# Access all the command-line arguments
# print(sys.argv)

# Access 1-onwards the command-line arguments
# print(sys.argv[1:])

# Defining filename
SAVED_DATA = "clipboard.json"

# Defining a script that will save data in a JSON file at a location of your choice. This JSON file will act as your clipboard storage.
def save_items(filepath, data):         
    with open(filepath, "w") as f:      # Opening a file in 'write' mode. Create one, otherwise override.
        json.dump(data, f)              # Dump the data into the file we opened

# Function call to write data to clipboard storage
# save_items("/Users/souravsarkar/Documents/Github/Automation/test.json", {"key":"value"})    # JSON is very similar to Python dictionaries

# Defining a function to read everything that we have stored in our clipboard storage
def load_items(filepath):
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            return data
    except:
        return {} # Error handling: Try to open the file. Otherwise return the empty dictionary.

# Checking the number of arguments
if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_items(SAVED_DATA)
    # print(f'You entered: ', command)
    # Checking which argument you entered
    if command == 'save':
        print(f'You entered: ',command)
        key = input('Enter a key: ')    # The key at which the data will be stored
        data[key] = clipboard.paste()   # Your clipboard data will be assigned to the key you saved above
        save_items(SAVED_DATA, data)    # Saving the data into the JSON file that we defined at the beginning
        print(f'SUCCESS! Your clipboard data is stored with this key: ',key)
    elif command == 'load':
        print(f'You entered: ',command)
    elif command == 'list':
        print(f'You entered: ',command)
    else:
        print(f'Unknown command!')
else:
    print(f'This command accepts only 1 command at a time.')