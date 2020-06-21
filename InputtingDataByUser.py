# file_name = input('Enter file name: ')
# print('The file name is: %s' % file_name)
print('------------------------------------------------------------')

# while True:
#
#     file_size_str = input('Enter the max file size (MB): ')
#
#     if file_size_str.isdecimal():
#         print('Size in KB is %s' % (int(file_size_str) * 1024))
#     break
#
# print('The max size is %s' % file_size_str)
print('------------------------------------------------------------')


#  Laboratory

def input_factor(factor_dict):
    factor_dict = {}

    for key in range(97, 100):
        key_of_value = str(chr(key))
        factor = input('Please insert value of factor {0:s}: '.format(*key_of_value))
        factor_dict.update({key_of_value: ''.join(str(f) for f in factor)})
    return factor_dict


def check_int():

    assigned_factor = input_factor(factor_dict={})
    print(assigned_factor)
    for key, value in assigned_factor.items():
        print(len(value))

        if value.find('-' or '+', 0, len(value)):

            if value.find('.' or ',', 0, len(value)):
                continue
            return value.isdigit()

        elif value.isdigit():

            if value.find('.' or ',', 0, len(value)):
                continue
            return value.isdigit()

        elif value.find('-' or '+', 0, len(value)) and value.find('.' or ',', 0, len(value)):
            return print('Factor %s is float. Please next time enter correct value of factor'
                         % key)

        elif value.find('.' or ',', 0, len(value)):
            return print('Factor %s is float. Please next time enter correct value of factor'
                         % key)

print(check_int())
