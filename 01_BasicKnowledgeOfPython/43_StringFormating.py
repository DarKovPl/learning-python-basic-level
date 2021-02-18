message_1 = 'Processing file: %s'
print(message_1 % 'file_1.txt')

message_2 = 'File %s has size %d KB'
print(message_2 % ('file_2.txt', 100))  # dodawać można określnoe typy do stringu

message_3 = 'File %20s has size %10d KB'
print(message_3 % ('file_3.txt', 100))  # rezerwować można miejsce na długość wpisu

message_4 = 'Processing file {0:s}'
print(message_4.format('file_04.txt'))

message_5 = 'File {0:s} has size {1:d}'
print(message_5.format('file_05.txt', 100))

message_5 = 'File {1:s} has size {0:d}'
print(message_5.format(100, 'file_5.txt'))

message_6 = 'File {0:20s} has size {1:10d}'
print(message_6.format('file_06', 100))

# Laboratory

helloMessage = "Hello %s!"
print(helloMessage % 'Kate')
print(helloMessage % 'Chris')

helloMessage = 'Hello {0:s}!'
print(helloMessage.format('Kate'))
print(helloMessage.format('Chris'))

helloMessage = '%s has %d %s'
print(helloMessage % ('Kate', 1, 'animal'))
print(helloMessage % ('Chris', 100000, '$'))

helloMessage = '{0:s} has {1:d} {2:s}'
print(helloMessage.format('Kate', 1, 'animal'))
print(helloMessage.format('Chris', 100000, '$'))

line = "{0:19s} {1:s} {2:6d} {3:s}"
print(line.format('ICE CREAM', 'cost', 3, '$'))
print(line.format('TRIP TO VENICE', 'cost', 119, '$'))
print(line.format('PIZZA HAWAII', 'cost', 6, '$'))
