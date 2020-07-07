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

def access_path(path_to_dir, name_of_file):
    # This function takes from the user access path to the directory and the
    # name of the file and checks whether or not the full path is correct.

    # here we are checking whether the entered path to the directory is correct
    if os.path.isdir(path_to_dir):

        # here is checking whether the entered file name is correct and the object is a file
        if os.path.isfile(path_to_dir + name_of_file):
            return path_to_dir, name_of_file

        else:
            print("Name of the file is incorrect or file doesn't exist")
            return quit()
    else:
        print("Inputted path to the directory is improper")
        return quit()


def information_of_file():
    # this function shows information about the file

    #  here we are assigning the results of work "access_path" function to "full_path_to_file" variable
    full_path_to_file = access_path(path_to_dir=input('Please type here the directory path:'),
                                    name_of_file=input('Now please input the name of the file:'))

    print('Date of latest modification in the file: ',
          time.localtime(os.path.getmtime(''.join([str(element) for element in full_path_to_file]))))
    print('Size of the file in bytes: ', os.path.getsize(''.join([str(element) for element in full_path_to_file])))
    print('Current directory is: ', os.getcwd())
    print('Relative path to the file is: ', os.path.relpath(''.join([str(element) for element in full_path_to_file])))


information_of_file()
