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
# print("Every person should have around", tasks_per_person, ' tasks.')
print('------------------------------------------------------------')

#  Laboratory

file_path = r'/tmp/orders.csv'

with open(file_path, "r") as file:
    for line in file:

        line = line.replace('\n', '')
        order = line.split(',')

        try:
            pharmacy_name = order[0]
            item = order[1]
            amount = int(order[2])
            print('Order from drugstore "%s", item "%s", amount %d' %
                  (pharmacy_name, item, amount))
        except ValueError as e:
            print('------------')
            print("Problem with line '%s' and the problem concern: %s"
                  % (line, e))
            print('************')

        except IndexError as e:
            print('------------')
            print("Problem with line '%s' and the problem concern: %s"
                  % (line, e))
            print('************')
        except:
            print('General error message: %s' % sys.exc_info()[0])

print("Processing finished")
