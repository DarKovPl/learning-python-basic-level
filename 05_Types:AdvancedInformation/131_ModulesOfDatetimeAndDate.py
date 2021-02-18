import datetime
import math
import random

print('Minimum and maximum: ', datetime.MINYEAR, ';', datetime.MAXYEAR)
print('--------------------------------------------------------')

d1 = datetime.timedelta(days=1, hours=2, minutes=-30)
print(d1)

d2 = datetime.timedelta(days=-1, hours=-2, minutes=-3)
print(d2)

print("timedelta sum: ", d1 + d2)
print('--------------------------------------------------------')

print('Today is: ', datetime.date.today(), '\n')

today = datetime.date.today()
days_to_pay = datetime.timedelta(days=7)
print('Today is: ', today)
print('Bills should be paid within: ', days_to_pay.days, 'days')
print('The bill should be paid till: ', today + days_to_pay, '\n')
print('--------------------------------------------------------')

end_of_the_world = datetime.date.max
print('The final end of world will happen (by Python):', end_of_the_world)
print(end_of_the_world.weekday(), '\n')
print('--------------------------------------------------------')

born_date = datetime.date(2000, 8, 15)
today = datetime.date.today()
print(today - born_date, '\n')
print('--------------------------------------------------------')

print('now()\t', datetime.datetime.now())
print('today()\t', datetime.datetime.today())
print('utcnow()\t', datetime.datetime.utcnow())
print('weekday()\t', datetime.datetime.today().weekday(), '\n')
print('--------------------------------------------------------')

print('%a \t\t - ', datetime.datetime.now().strftime('%a'))
print('%A \t\t - ', datetime.datetime.now().strftime('%A'))
print('%w \t\t - ', datetime.datetime.now().strftime('%w'))
print('%a %A %w - ', datetime.datetime.now().strftime('%a %A %w'))
print('%Y-%m-%d_%H_%S_%f - ',
      datetime.datetime.now().strftime('%Y-%m-%d_%H_%S_%f'))
print('--------------------------------------------------------')

#  Laboratory

input_data = [0, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
factor_table = [0, 0.01, 0.02, 0.03, 0.05, 0.08,
                0.13, 0.21, 0.34, 0.55, 0.89]

print(len(input_data), len(factor_table))
print('--------------------------------------------------------')

if len(input_data) == len(factor_table):

    for element_in_input_data in range(len(input_data)):
        min_value = input_data[element_in_input_data] - factor_table[element_in_input_data] \
                    * input_data[element_in_input_data]
        max_value = input_data[element_in_input_data] + factor_table[element_in_input_data] \
                    * input_data[element_in_input_data]

        min_integer = math.floor(min_value)
        max_integer = math.ceil(max_value)

        print('min_value= %.2f ' % min_value, 'max_value= %.2f' % max_value, '\n', min_integer,
              input_data[element_in_input_data], max_integer)

else:
    print('input_data and factor_table need to have equal number'
          ' of elements')
print('--------------------------------------------------------')

factor_table = []

for counter in range(len(input_data)):
    factor_table.append(random.random())

    if counter == len(input_data):
        break

if len(input_data) == len(factor_table):

    for element_in_input_data in range(len(input_data)):

        if len(input_data) == len(factor_table):
            min_value = input_data[element_in_input_data] - factor_table[element_in_input_data] \
                        * input_data[element_in_input_data]
            max_value = input_data[element_in_input_data] + factor_table[element_in_input_data] \
                        * input_data[element_in_input_data]

            min_integer = math.floor(min_value)
            max_integer = math.ceil(max_value)

            print('min_value= %.2f ' % min_value, 'max_value= %.2f' % max_value, '\n', min_integer,
                  input_data[element_in_input_data], max_integer)

else:
    print('input_data and factor_table need to have equal number'
          ' of elements')
print('--------------------------------------------------------')

print(datetime.datetime.now().strftime('%Y'), datetime.datetime.now().strftime('%m'),
      datetime.datetime.now().strftime('%d'))
print(datetime.datetime.today().strftime('%Y-%m-%d'))
