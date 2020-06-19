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
    assigned_factor = input_factor(factor_dict='')

    for value in assigned_factor.values():

        if value[0] == ('-' or '+'):
            return value[1:].isdigit()

        elif value[0].isdigit():
            return value.isdigit()

        else:
            print('Is not float:')
            break



print(check_int())
