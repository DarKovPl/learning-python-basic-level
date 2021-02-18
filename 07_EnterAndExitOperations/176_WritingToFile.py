file_name = '/tmp/output.txt'

line = 'Europe'

cities = ['London', 'Berlin', 'Paris', 'Warsaw', 'Madrid', 'Rome']

file = open(file_name, 'w+')

file.write(line)
file.write('\n')
# file.writelines(cities + list('\n'))

for city in cities:
    file.write(city+'\n')

file.close()
