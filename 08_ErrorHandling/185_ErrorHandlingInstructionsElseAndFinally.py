import sys

# tasks_per_person = 0
#
# try:
#     tasks = 32
#     persons_string = input('How many persons are there in the team? ')
#     persons = int(persons_string)
#
#     tasks_per_person = tasks / persons
#
# except ValueError as e:
#     print('Sorry - you need to enter an integer number %s.' % e)
#
# except ZeroDivisionError as e:
#     print('Sorry - you need to enter value > 0. %s' % e)
#
# except:
#     print('Something went wrong.....', sys.exc_info()[0])
#
# else:
#     print("Every person should have around", tasks_per_person, ' tasks.')
#
# finally:
#     print('Script finished with/without errors')
print('------------------------------------------------------------')

# Laboratory

try:
    line = input('What is the highest price for Udemy course that you will be able to pay? ')
    value = int(line)
    path_to_file = input('Please enter the path to file here: ')

    with open(path_to_file, 'w+') as file:
        file.write(line)
    print('The value saved in file is %d' % value)

except FileNotFoundError as e:
    print('Error opening file %s' % e)

except ValueError as e:
    print("The value entered cannot be converted to a number. Details: %s" % e)

except:
    print('Sorry- we have an error')

else:
    print("Actions completed successfully")