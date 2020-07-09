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

yes = 'Y'

if not os.path.isdir(data_input_catalog):
    os.makedirs(today_input_catalog)

else:
    if yes == input("This directory: %s is already existing, if you want to delete it,"
                    " input 'y' here. ->: " % today_input_catalog).upper():
        shutil.rmtree(os.path.split(today_input_catalog)[0])
        print("Run the program again to create a new catalog with today's date.")

    else:
        print("New catalog %s wasn't created because there was already a catalog with the same name,"
              " and the old one wasn't deleted." % today_input_catalog)


if not os.path.isdir(today_output_catalog):
    os.makedirs(today_output_catalog)

else:
    if yes == input("This directory: %s is already existing, if you want to delete it,"
                    " input 'y' here. ->: " % today_output_catalog).upper():
        shutil.rmtree(os.path.split(today_output_catalog)[0])
        print("Run the program again to create a new catalog with today's date.")

    else:
        print("New catalog %s wasn't created because there was already a catalog with the same name,"
              " and the old one wasn't deleted." % today_output_catalog)

today_output_catalog = os.path.join(data_output_catalog, today.strftime("%Y-%m-%d"))
is_input_catalog_ok = os.path.isdir(data_input_catalog)
