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

data_input_catalog = r'/tmp/data_input'
data_output_catalog = r'/tmp/data_output'
today = datetime.date.today()

today_output_catalog = os.path.join(data_output_catalog, today.strftime("%Y-%m-%d"))
today_input_catalog = os.path.join(data_input_catalog, today.strftime("%Y-%m-%d"))

directory_or_file = ''

yes = 'Y'

if os.path.isfile(data_input_catalog):
    shutil.rmtree(data_input_catalog)

elif not os.path.isdir(data_input_catalog):
    os.mkdir(data_input_catalog)


if not os.path.isfile(today_input_catalog):
    os.mknod(today_input_catalog)

else:
    if os.path.isfile(today_input_catalog):
        directory_or_file = 'file'

    else:
        directory_or_file = 'directory'

    if directory_or_file == 'directory':
        shutil.rmtree(os.path.split(today_input_catalog)[1])

    elif directory_or_file == 'file' and \
            yes == input("This %s: %s is already existing, if you want to delete it,"
                         " input 'y' here. ->: " % (directory_or_file, today_input_catalog)).upper():
        shutil.rmtree(os.path.split(today_input_catalog)[1])
        print("Run the program again to create a correct structure catalogs with today's date.")

    else:
        print("New file %s wasn't created because there was already a %s with the same name,"
              " and the old one wasn't deleted." % (today, directory_or_file))

if not os.path.isdir(today_output_catalog):
    os.makedirs(today_output_catalog)

else:
    if os.path.isfile(today_input_catalog):
        directory_or_file = 'FILE'

    else:
        directory_or_file = 'directory'

    if yes == input("This %s: %s is already existing, if you want to delete it,"
                    " input 'y' here. ->: " % (directory_or_file, today_output_catalog)).upper():
        shutil.rmtree(os.path.split(today_output_catalog)[0])
        print("Run the program again to create a correct structure catalogs with today's date.")

    else:
        print("New catalog %s wasn't created because there was already a %s with the same name,"
              " and the old one wasn't deleted." % (today_output_catalog, directory_or_file))
