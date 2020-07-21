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
# except:
#     print('Something went wrong.....', sys.exc_info()[0])
#
# print("Every person should have around", tasks_per_person, ' tasks.')

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

            print('Order from drugstore %s, item %s, amount %d' % (pharmacy_name, item, amount))

        except:
            print('------------')
            print("Something wrong in line: %d." % sys.exc_info()[-1].tb_lineno,
                  'Information of an exception: %s' % sys.exc_info()[0])
            print('************')

print("Processing finished")
