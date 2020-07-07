import os
import time

print('Current directory is: ', os.getcwd())
os.chdir('/home/darek/Projects/learning_python')
print('Current directory is: ', os.getcwd())

current_dir = os.getcwd()
file_name = 'results.txt'
full_path = os.path.join(current_dir, file_name)
print('\nThe constructed file path is: ', full_path)
print('------------------------------------------------------------')

relative_path = 'output.txt'
print('\nThe absolute path is: ', os.path.abspath(relative_path))
print('------------------------------------------------------------')

file_path = r"/tmp/results.txt"
print('\nThe file name part is: ', os.path.basename(file_path))
print('The directory part is: ', os.path.dirname(file_path))
print('------------------------------------------------------------')

print('\nIs file existing? ', os.path.exists(file_path))
print('------------------------------------------------------------')

if os.path.exists(file_path):
    print('\nLast modify date is: ', os.path.getmtime(file_path))
    print('\nLast modify date is: ', time.localtime(os.path.getmtime(file_path)))
    print('\nFile size is: ', os.path.getsize(file_path))
    print('\nIs it a dir? ', os.path.isdir(file_path))
    print('\nIs it a file? ', os.path.isfile(file_path))
    print('\nPath splitted: ', os.path.split(file_path))
    print('\nOnly file name part: ', os.path.split(file_path)[1])
    print('\nPath splitted into drive: ', os.path.splitdrive(file_path))
    print('Only drive: ', os.path.splitdrive(file_path)[0])


# Laboratory

def access_path(path, file):
    # This function takes from the user access path to the directory and the
    # name of the file and checks whether or not the full path is correct.

    path_to_dir = path
    name_of_file = file

    if os.path.isdir(path_to_dir):
        if os.path.isfile(path_to_dir + name_of_file):
            return str(path_to_dir), str(name_of_file)
        else:
            print("Name of the file is incorrect or file doesn't exist")
            return quit()
    else:
        print("Inputted path to the directory is improper")
        return quit()


def information_of_file():
    # this function shows information about the file

    full_path_to_file = access_path(path=input('Please type here the directory path:'),
                                    file=input('Now please input the name of the file:'))
    
    print(time.localtime(os.path.getatime(full_path_to_file)))


information_of_file()
