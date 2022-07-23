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

# Checking the number of arguments
if len(sys.argv) == 2:
    command = sys.argv[1]
    # print(f'You entered: ', command)
    # Checking which argument you entered
    if command == 'save':
        print(f'You entered: ',command)
    elif command == 'load':
        print(f'You entered: ',command)
    elif command == 'list':
        print(f'You entered: ',command)
    else:
        print(f'Unknown command!')
else:
    print(f'this command only accepts 1 command at a time.')