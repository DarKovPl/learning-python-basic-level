file = open(r'/tmp/data_output/2020-07-16', 'r')

content = file.read()
print(content)

file.close()
print('------------------------------------------------------------')

with open(r'/tmp/data_output/2020-07-16', 'r') as file:
    content = file.read()
    print(content)
print('------------------------------------------------------------')

with open(r'/tmp/.bash_history', 'r') as file:
    for line in file:
        print(line)
print('------------------------------------------------------------')

file = open(r'/tmp/.bash_history', 'r')

fragment = file.read(20)

while fragment:
    print(file.tell(), fragment)
    fragment = file.read(20)

file.close()
print('------------------------------------------------------------')

#  Laboratory

file_path = r'/tmp/data_input/orders.csv'

with open(file_path) as file:

    for line in file:
        line = line.rstrip('\n')
        order = line.split(',')

        if len(order) == 3:
            print('Order from drugstore %s, item %s, amount %s' % (order[0], order[1], order[2]))
        else:
            print("Line %s malformed!!!" % line)
print("Processing finished")