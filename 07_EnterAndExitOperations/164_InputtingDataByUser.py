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


# Laboratory

def input_factors():
    #  This function was created for receiving factors from user.
    factor_dict = {}

    for key in range(97, 100):
        key_of_value = str(chr(key))  # Loop receive alphabet characters from table of ASCII for names factors
        factor = input('Please insert value of factor {0:s}: '.format(*key_of_value))
        factor_dict.update({key_of_value: ''.join(str(f) for f in factor)})  # Dictionary "factor_dict" is updating
        # about key and value

    return factor_dict


def check_the_factor_is_integer():
    # This function is able to verify correct value of inputted factors is integer, is string or is float.
    # Float or string is incorrect value in this exercise.

    factors = input_factors()  # Here we are assigning result of work "input_factors" function to variable "factors"

    for key, value in factors.items():

        if re.findall("[-+]", value):  # Here we are using regular expression module for find plus or minus in value

            if re.findall("[.,]", value):  # Here we are using regular expression module for find dot or comma
                # in value. Float type is wrong parameter. User is informed what a mistake he was did.
                return print('Coefficient "%s" is float. Please next time enter correct (integer)'
                             ' value of coefficient' % key), quit()

            elif key == 'a' and value == '0':  # If parameter "a" is equal zero is impossible dividing
                return print('Factor "%s" equals zero. Fix it!' % key), quit()

            else:

                if value[1:].isdigit():  # Here we are checking value is a digit from index 1 to the end of
                    # digits in a value
                    continue

                else:
                    return print('Factor "%s" in not a digit. Fix it!' % key), quit()

        else:  # difference from if: value without plus or minus sign

            if re.findall("[.,]", value):
                return print('Coefficient "%s" is float. Please next time enter correct (integer)'
                             ' value of coefficient' % key), quit()

            elif key == 'a' and value == '0':
                return print('Factor "%s" equals zero. Fix it!' % key), quit()

            else:

                if value[0:].isdigit():
                    continue

                else:
                    return print('Factor "%s" in not a digit. Fix it!' % key), quit()

    checked_values = factors  # Here we are assigning variable "factors" to "checked_value". Just for easier to read.
    print('Every inputted value is correct')  # If user see this on his computer this mean all coefficients are correct

    return checked_values


def counting_delta_and_zero_of_function():
    # This function counting delta and zero of function.

    numerical_coefficients = check_the_factor_is_integer()  # Here we are assigning result of work
    # "check_the_factor_is_integer" function to variable "numerical_coefficients"

    delta = pow(int(numerical_coefficients.get('b')), 2) - 4 * int(numerical_coefficients.get('a')) \
            * int(numerical_coefficients.get('c'))
    print(delta)

    if delta < 0:
        return print('Delta is below zero. There is no chance to count this'), quit()

    elif delta == 0:
        x_1 = ((-int(numerical_coefficients.get('b'))) - sqrt(delta)) / (2 * int(numerical_coefficients.get('a')))
        return print('x_1= ', round(x_1, 2)), quit()

    else:
        x_1 = (-int(numerical_coefficients.get('b')) - sqrt(delta)) / (2 * int(numerical_coefficients.get('a')))
        x_2 = (-int(numerical_coefficients.get('b')) + sqrt(delta)) / (2 * int(numerical_coefficients.get('a')))
        return print('x_1= ', round(x_1, 2), '\n', 'x_2= ', round(x_2, 2)), quit()


counting_delta_and_zero_of_function()
