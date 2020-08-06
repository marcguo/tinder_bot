import os

# This defines the current Python file's path.
DIR_PATH = os.path.dirname(os.path.realpath(__file__))
# This defines the file name of the local log file.
FILE_NAME = DIR_PATH + '/log.txt'

# Method to write to the local log file.
def log(content):
    with open(FILE_NAME, 'a') as file:
        file.write(str(content) + '\n')
        
def remove():
# Remove the existing log file.
    try:
        os.remove(FILE_NAME)
    except OSError:
        pass
