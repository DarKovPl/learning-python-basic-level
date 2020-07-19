import os

# web_addresses = []
# line = input('Please enter here a web page address: ')
#
# while not len(line) == 0:
#     web_addresses.append(line)
#     line = input('Please enter here a web page address: ')
#
# dir_name = os.getcwd()
#
# file_name = input('Please enter here a name of the file: ')
# file_path = os.path.join(dir_name, file_name)
#
# with open(file_path, 'a+') as file:
#     for address in web_addresses:
#         file.write(address + ''.join('\n'))

# print('------------------------------------------------------------')
#
# path_to_file = input('Please enter here a path to the file: ')
#
# while not os.path.isfile(path_to_file):
#     print('This is an incorrect path to the file. Please try again.')
#     path_to_file = input('Please enter here a path to the file: ')
#
# web_addresses_1 = []
#
# with open(path_to_file, 'r') as opened_file:
#     reading_file = opened_file.readlines()
#
#     while not len(reading_file) == 0:
#         web_addresses_1.append(reading_file.pop(0))
#         web_addresses_1 = ' '.join(web_addresses_1).replace('\n', ' ').split()
#
#         dir_path = os.path.dirname(path_to_file)
#         pl_file_name = 'webs_pl.txt'
#         other_file_name = 'webs_other.txt'
#
#         if not str(web_addresses_1[0].split('.')).find('pl') == -1:
#             print('This address is from Poland: ', web_addresses_1[0])
#
#             with open(os.path.join(dir_path, pl_file_name), 'a+') as pl_address:
#                 pl_address.write(web_addresses_1.pop(0)+'\n')
#
#         else:
#             print('This address is NOT from Poland: ', web_addresses_1[0])
#
#             with open(os.path.join(dir_path, other_file_name), 'a+') as other_address:
#                 other_address.write(web_addresses_1.pop(0)+'\n')
print('------------------------------------------------------------')

