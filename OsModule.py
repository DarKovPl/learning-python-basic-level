import os
import time

print('Current directory is: ', os.getcwd())

current_dir = os.getcwd()
file_name = 'results.txt'
full_path = os.path.join(current_dir, file_name)
print('\nThe constructed file path is: ', full_path)
print('------------------------------------------------------------')

relative_path = 'output.txt'
print('\nThe absolute path is: ', os.path.abspath(relative_path))
print('------------------------------------------------------------')

file_path = r'/tmp/results.txt'
print('\nThe file name part is: ', os.path.basename(file_path))
print('The directory part is: ', os.path.dirname(file_path))
print('------------------------------------------------------------')

print('\nIs file existing? ', os.path.exists(file_path))
