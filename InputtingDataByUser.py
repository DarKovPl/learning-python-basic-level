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
        key_of_value = [chr(key)]
        factor = input('Please insert value of factor {0:s}: '.format(*key_of_value))
        print(factor)
        factor_dict.update(dict(zip(key_of_value, factor.join([str(digit) for digit in factor]))))
    print(factor_dict)
    return factor_dict


def check_int():
    assigned_factor = input_factor(factor_dict='')

    for value in assigned_factor.values():
        if str(value).isdigit():
            print(value)

    return str(value).isdigit()


print(check_int())
