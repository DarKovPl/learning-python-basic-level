import os

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

while True:

    file_name = input('Enter path to results.txt file: ')

    if os.path.isfile(file_name):
        print('The results file is %s' % file_name)
        break

    else:
        print('Name of the file is invalid. Try again.')