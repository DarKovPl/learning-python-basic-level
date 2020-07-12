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


today = datetime.date.today()
# today_output_file = os.path.join(data_output_catalog, today.strftime("%Y-%m-%d"))
yes = 'Y'


def input_tree_structure(data_input_catalog=r'/tmp/data_input'):
    today_input_file = os.path.join(data_input_catalog, today.strftime("%Y-%m-%d"))

    while not (os.path.isdir(data_input_catalog) and os.path.isfile(today_input_file)):

        if os.path.isfile(data_input_catalog):
            os.remove(data_input_catalog)
            print('%s was a file, and it was deleted.' % data_input_catalog)

        elif os.path.isdir(today_input_file):
            os.rmdir(today_input_file)
            print('%s was a directory, and it was deleted.' % today_input_file)

        elif not os.path.isdir(data_input_catalog):
            os.mkdir(data_input_catalog)
            print('Directory %s was successfully created' % data_input_catalog)

        elif not os.path.isfile(today_input_file):
            os.mknod(today_input_file)
            print('File %s was successfully created' % today_input_file)


    # if len(os.listdir(data_input_catalog)) == 0:
    #
    #     if yes == input("This empty catalog: %s is already existing if you want to delete it "
    #                     "and create a new one with today's date type 'y' here ->: "
    #                     % data_input_catalog).upper():
    #         os.rmdir(data_input_catalog)
    #         os.mkdir(data_input_catalog)
    #         return print('The old directory was deleted and the new one was created: %s'
    #                      % data_input_catalog)
    #
    #     else:
    #         return print("New directory wasn't created because there was already directory (%s) with the same name, "
    #                      " and the old one wasn't deleted." % data_input_catalog)
    #
    # else:
    #     print('%s is not empty.' % data_input_catalog)
    #
    #     if yes == input("If you want to delete it with its contents and a create new empty directory"
    #                     " %s type 'y' here ->: " % data_input_catalog).upper():
    #         shutil.rmtree(data_input_catalog)
    #         os.mkdir(data_input_catalog)
    #         return print('All elements and the old directory were deleted. New empty directory was created %s.'
    #                      % data_input_catalog)
    #
    #     else:
    #         create_time = time.ctime(os.path.getctime(data_input_catalog))
    #         age_of_catalog = datetime.datetime.today() - datetime.datetime.fromtimestamp(
    #             os.path.getctime(data_input_catalog))
    #         return print('Nothing was deleted and you will be writing new log files into the old catalog. '
    #                      'Catalog was created %s. The directory was created %.7s ago. ' % (create_time, age_of_catalog))


input_tree_structure()
print('------------------------------------------------------------')

# def output_tree_structure(data_output_catalog=r'/tmp/data_output'):
#     while not os.path.isdir(data_output_catalog):
#
#         if os.path.isfile(data_output_catalog):
#             os.remove(data_output_catalog)
#             print('%s was a file, and it was deleted.' % data_output_catalog)
#
#         else:
#             os.mkdir(data_output_catalog)
#             return print('Directory %s was successfully created' % data_output_catalog)
#
#     if len(os.listdir(data_output_catalog)) == 0:
#
#         if yes == input("This empty catalog: %s is already existing if you want to delete it "
#                         "and create a new one with today's date type 'y' here ->: "
#                         % data_output_catalog).upper():
#             os.rmdir(data_output_catalog)
#             os.mkdir(data_output_catalog)
#             return print('The old directory was deleted and the new one was created: %s'
#                          % data_output_catalog)
#
#         else:
#             return print("New directory wasn't created because there was already directory (%s) with the same name, "
#                          "and the old one wasn't deleted." % data_output_catalog)
#
#     else:
#         print('%s is not empty.' % data_output_catalog)
#
#         if yes == input("If you want to delete it with its contents and a create new empty directory"
#                         " %s type 'y' here ->: " % data_output_catalog).upper():
#             shutil.rmtree(data_output_catalog)
#             os.mkdir(data_output_catalog)
#             return print('All elements and the old directory were deleted. New empty directory was created %s.'
#                          % data_output_catalog)
#
#         else:
#             create_time = time.ctime(os.path.getctime(data_output_catalog))
#             age_of_catalog = datetime.datetime.today() - datetime.datetime.fromtimestamp(
#                 os.path.getctime(data_output_catalog))
#             return print('Nothing was deleted and you will be writing new log files into the old catalog. '
#                          'Catalog was created %s. The directory was created %.7s ago. ' % (create_time, age_of_catalog))
#
#
# output_tree_structure()
