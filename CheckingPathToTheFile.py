import os
import datetime
import shutil

file_is_ok = False

# while not file_is_ok:
#
#     file_name = input('Enter path to results.txt file: ')
#
#     if os.path.isfile(file_name):
#         file_is_ok = True
#         print('The results file is %s' % file_name)
#
#     else:
#         print('Name of the file is invalid. Try again.')
print('------------------------------------------------------------')

# while True:
#
#     file_name = input('Enter path to results.txt file: ')
#
#     if os.path.isfile(file_name):
#         print('The results file is %s' % file_name)
#         break
#
#     else:
#         print('Name of the file is invalid. Try again.')
print('------------------------------------------------------------')

# Laboratory


data_output_catalog = r'/tmp/data_output'
today = datetime.date.today()

# today_output_catalog = os.path.join(data_output_catalog, today.strftime("%Y-%m-%d"))
# today_input_catalog = os.path.join(data_input_catalog, today.strftime("%Y-%m-%d"))



yes = 'Y'


def input_tree_structure(data_input_catalog=r'/tmp/data_input'):

    while not os.path.isdir(data_input_catalog):

        if os.path.isfile(data_input_catalog):
            os.remove(data_input_catalog)
            print('%s was a file, and it was deleted.' % data_input_catalog)

        else:
            os.mkdir(data_input_catalog)
            return print('Directory %s was successfully created' % data_input_catalog)

    if len(os.listdir(data_input_catalog)) == 0:

        if yes == input("This empty catalog: %s is already existing if you want to delete it "
                        "and create a new one with today's date type 'y' here ->: "
                        % data_input_catalog).upper():
            os.rmdir(data_input_catalog)
            os.mkdir(data_input_catalog)
            return print('The old directory was deleted and the new one was created: %s'
                         % data_input_catalog)

        else:
            return print("New directory wasn't created because there was already directory (%s) with the same name, "
                         " and the old one wasn't deleted." % data_input_catalog)

    else:
        print('%s is not empty.' % data_input_catalog)

        if yes == input("If you want to delete it with its contents and a create new empty directory"
                        " %s type 'y' here ->: " % data_input_catalog).upper():
            shutil.rmtree(data_input_catalog)
            os.mkdir(data_input_catalog)
            return print('All elements and the old directory were deleted. New empty directory was created %s.'
                         % data_input_catalog)

        else:
            return print('Nothing was deleted, and the structure is improper. Program ends work.')


input_tree_structure()

# if not os.path.isfile(today_input_catalog):
#     os.mknod(today_input_catalog)
#
# else:
#     if os.path.isfile(today_input_catalog):
#         directory_or_file = 'file'
#
#     else:
#         directory_or_file = 'directory'
#
#     if directory_or_file == 'directory':
#         shutil.rmtree(os.path.split(today_input_catalog)[1])
#
# if not os.path.isdir(today_output_catalog):
#     os.makedirs(today_output_catalog)
#
# else:
#     if os.path.isfile(today_input_catalog):
#         directory_or_file = 'FILE'
#
#     else:
#         directory_or_file = 'directory'
#
#     if yes == input("This %s: %s is already existing, if you want to delete it,"
#                     " input 'y' here. ->: " % (directory_or_file, today_output_catalog)).upper():
#         shutil.rmtree(os.path.split(today_output_catalog)[0])
#         print("Run the program again to create a correct structure catalogs with today's date.")
#
#     else:
#         print("New catalog %s wasn't created because there was already a %s with the same name,"
#               " and the old one wasn't deleted." % (today_output_catalog, directory_or_file))
