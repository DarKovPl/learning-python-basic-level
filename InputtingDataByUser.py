import re
from math import sqrt

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

def input_factors():
    factor_dict = {}

    for key in range(97, 100):
        key_of_value = str(chr(key))
        factor = input('Please insert value of factor {0:s}: '.format(*key_of_value))
        factor_dict.update({key_of_value: ''.join(str(f) for f in factor)})

    return factor_dict


def check_int():
    factors = input_factors()

    for key, value in factors.items():

        if re.findall("[-+]", value):

            if re.findall("[.,]", value):
                return print('Coefficient "%s" is float. Please next time enter correct value of coefficient'
                             % key), quit()
            elif value[0] == '0':
                return print('Factor "%s" equals zero. Fix it!' % key[0]), quit()

            else:
                if value[1:].isdigit():
                    continue
                else:

                    return print('Factor "%s" in not a digit. Fix it!' % key), quit()

        else:
            if re.findall("[.,]", value):
                return print('Coefficient "%s" is float. Please next time enter correct value of coefficient'
                             % key), quit()
            elif value[0] == '0':
                return print('Factor "%s" equals zero. Fix it!' % key[0]), quit()

            else:
                if value[0:].isdigit():
                    continue
                else:
                    return print('Factor "%s" in not a digit. Fix it!' % key), quit()

    checked_values = factors
    print('Every inputted value is correct')
    return checked_values


def counting_delta_and_zero_of_function():
    numerical_coefficients = check_int()

    delta = pow(int(numerical_coefficients.get('b')), 2) - 4 * int(numerical_coefficients.get('a')) * \
            int(numerical_coefficients.get('c'))
    print(delta)

    if delta < 0:

        return print('Delta is below zero. There is no chance to count this'), quit()

    elif delta == 0:

        x_1 = ((-int(numerical_coefficients.get('b'))) - sqrt(delta)) / (2 * int(numerical_coefficients.get('a')))
        return print(x_1), quit()

    else:

        x_1 = (-int(numerical_coefficients.get('b')) - sqrt(delta)) / (2 * int(numerical_coefficients.get('a')))
        x_2 = (-int(numerical_coefficients.get('b')) + sqrt(delta)) / (2 * int(numerical_coefficients.get('a')))
        return print('x_1= ', round(x_1, 2), '\n', 'x_2= ', round(x_2, 2))


counting_delta_and_zero_of_function()
