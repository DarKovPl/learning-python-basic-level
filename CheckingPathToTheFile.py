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
    # this function was created for creating and checking the correct structure of 'data_input_catalog'
    # and also for creating a daily file.

    # here we are assign to variable a correct path to the "today file"
    today_input_file = os.path.join(data_input_catalog, today.strftime("%Y-%m-%d"))

    # here we are assigning the path to the "today file" in "data_output_catalog" to check if the file
    # has been already moved
    is_today_file_in_data_output = os.path.join(data_output_catalog, os.path.split(today_input_file)[1])

    # here we are split path for better print. We will printed only the needed element, not a whole path.
    split_path_dir_in = os.path.split(data_input_catalog)
    split_path_file_in = os.path.split(today_input_file)

    # this loop ends at work when: "data_input_catalog" is created and is a directory, "today_input_file" is created
    # and is a file, or "is_today_file_in_data_output" file already exists in "data_output_file".
    while not (os.path.isdir(data_input_catalog) and (os.path.isfile(today_input_file)
                                                      or os.path.isfile(is_today_file_in_data_output))):

        if os.path.isfile(data_input_catalog):
            os.remove(data_input_catalog)  # if file- delete
            print("'%s' was a file, and it was deleted." % split_path_dir_in[1])

        elif os.path.isdir(today_input_file):
            os.rmdir(today_input_file)  # if directory- delete
            print("'%s' was a directory, and it was deleted." % split_path_file_in[1])

        elif not os.path.isdir(data_input_catalog):
            os.mkdir(data_input_catalog)  # if not exist- create
            print("Directory '%s' was successfully created" % split_path_dir_in[1])

        elif not os.path.isfile(today_input_file):
            os.mknod(today_input_file)  # if not exist- create
            print("File '%s' was successfully created" % split_path_file_in[1])

    # here we return three variable for use in another function.
    return today_input_file, is_today_file_in_data_output, data_output_catalog


print('------------------------------------------------------------')
input_tree_structure()
print('------------------------------------------------------------')


def output_tree_structure(set_export_hour=datetime.time(18, 59, 59)):
    #   This function was created for creating and checking the correct structure of 'data_output_catalog' and also
    #   for moving a "daily file" from "data_input_catalog" to "data_output_catalog". Function is able to move a
    #   "today file" automatically after 19:00. Function is also able to print a message for the user to do a data
    #   backup  after 30 days.

    # here we are assigning a path and name the "today file" in the "data_input_catalog"
    input_file_from_source = input_tree_structure()[0]

    # here we are assigning a path and name the "today file" in the "data_output_catalog" for checking
    # if there already exists.
    is_today_file_in_output_dir = input_tree_structure()[1]

    # here we are assigning "data_output_catalog" path to variable
    data_output_catalog_from_source = input_tree_structure()[2]

    current_hour = time.strftime("%H:%M:%S")

    # here we are split path for better print. We will printed only the needed element, not a whole path
    split_path_dir_out = os.path.split(data_output_catalog_from_source)
    split_path_input_file_from_source = os.path.split(input_file_from_source)

    # this loop ends at work when: "data_output_catalog" is created and is a directory, "is_today_file_in_output_dir"
    # is moved from "data_input_catalog" and is a file.
    while not (os.path.isdir(data_output_catalog_from_source) and os.path.isfile(is_today_file_in_output_dir)):

        if os.path.isfile(data_output_catalog_from_source):
            os.remove(data_output_catalog_from_source)  # if file- delete
            print("'%s' was a file, and it was deleted." % split_path_dir_out[1])

        elif not os.path.isdir(data_output_catalog_from_source):
            os.mkdir(data_output_catalog_from_source)  # if directory- delete
            print("Directory '%s' was successfully created" % split_path_dir_out[1])

        elif (not os.path.isfile(is_today_file_in_output_dir)) and (str(set_export_hour) < current_hour):
            # if not exist and is after 19:00- move
            shutil.move(input_file_from_source, data_output_catalog_from_source)
            print("File '%s' was successfully moved" % split_path_input_file_from_source[1])
            continue

    # getting from "data_output" a create time of the directory
    catalog_create_time_out = time.ctime(os.path.getctime(data_output_catalog_from_source))

    # count age data_output_directory
    catalog_age_out = datetime.datetime.today() - datetime.datetime.fromtimestamp(
        os.path.getctime(data_output_catalog_from_source))
    print('Directory created date: %s and it was %.8s ago. ' % (catalog_create_time_out, catalog_age_out))

    # if data_output_catalog has more than 30 days then user get a message to do backup.
    if str(catalog_age_out) > '30':
        print("30 days passed. You have to do a backup of data and clear the '%s' directory."
              % split_path_dir_out[1])

    # if you want to check it up, uncomment this part of code. Run the code again after one minute,
    # and you get a message.

    # if str(catalog_age_out) > '0:01:00':
    #     print("30 days passed. You have to do a backup of data and clear the '%s' directory."
    #           % split_path_dir_out[1])


output_tree_structure()
