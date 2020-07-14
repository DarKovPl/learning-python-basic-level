import os
import datetime
import shutil
import time

# file_is_ok = False

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

def input_tree_structure(data_input_catalog=r'/tmp/data_input', data_output_catalog=r'/tmp/data_output',
                         today=datetime.date.today()):
    # this function was created for create and check the correct structure of data_input_catalog with daily logs file

    today_input_file = os.path.join(data_input_catalog, today.strftime("%Y-%m-%d"))
    is_today_output_file = os.path.join(data_output_catalog, os.path.split(today_input_file)[1])

    split_path_dir_in = os.path.split(data_input_catalog)
    split_path_file_in = os.path.split(today_input_file)

    while not (os.path.isdir(data_input_catalog) and (os.path.isfile(today_input_file)
                                                      or os.path.isfile(is_today_output_file))):

        if os.path.isfile(data_input_catalog):
            os.remove(data_input_catalog)
            print("'%s' was a file, and it was deleted." % split_path_dir_in[1])

        elif os.path.isdir(today_input_file):
            os.rmdir(today_input_file)
            print("'%s' was a directory, and it was deleted." % split_path_file_in[1])

        elif not os.path.isdir(data_input_catalog):
            os.mkdir(data_input_catalog)
            print("Directory '%s' was successfully created" % split_path_dir_in[1])

        if not os.path.isfile(today_input_file):
            os.mknod(today_input_file)
            print("File '%s' was successfully created" % split_path_file_in[1])

    return today_input_file, is_today_output_file, data_output_catalog


print('------------------------------------------------------------')


def output_tree_structure():
    # this function was created for create and check the correct structure of data_output_catalog with daily logs file

    input_file_from_source = input_tree_structure()[0]
    output_file_from_source = input_tree_structure()[1]
    data_output_catalog_from_source = input_tree_structure()[2]

    set_export_hour = datetime.time(18, 59, 59)
    currently_hour = time.strftime("%H:%M:%S")
    print(currently_hour)
    split_path_dir_out = os.path.split(data_output_catalog_from_source)
    split_path_input_file_from_source = os.path.split(input_file_from_source)

    while not (os.path.isdir(data_output_catalog_from_source) and os.path.isfile(output_file_from_source)):

        if os.path.isfile(data_output_catalog_from_source):
            os.remove(data_output_catalog_from_source)
            print("'%s' was a file, and it was deleted." % split_path_dir_out[1])

        elif not os.path.isdir(data_output_catalog_from_source):
            os.mkdir(data_output_catalog_from_source)
            print("Directory '%s' was successfully created" % split_path_dir_out[1])

        elif (not os.path.isfile(output_file_from_source)) and (str(set_export_hour) < currently_hour):
            shutil.move(input_file_from_source, data_output_catalog_from_source)
            print("File '%s' was successfully moved" % split_path_input_file_from_source[1])
            continue
    catalog_create_time_out = time.ctime(os.path.getctime(data_output_catalog_from_source))
    catalog_age_out = datetime.datetime.today() - datetime.datetime.fromtimestamp(
        os.path.getctime(data_output_catalog_from_source))
    print('Directory created date: %s and it was %.8s ago. ' % (catalog_create_time_out, catalog_age_out))

    if str(catalog_age_out) > '30':
        print("30 days passed. You have to do a backup of data and clear the '%s' directory."
              % split_path_dir_out[1])


output_tree_structure()
