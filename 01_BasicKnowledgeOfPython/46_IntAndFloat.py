import sys

five = 5
three = 3

print(three * five)
print(type(three))
print(type(five * three))
print(five / three)
print(type(five / three))

print(sys.maxsize)
veryBigValue = 9999999999999999999999999999999999999999999999999
print(veryBigValue)
print(veryBigValue + 1)
print(type(veryBigValue))

print((veryBigValue + 1) / 2)
print(type((veryBigValue + 1) / 2))

print(five // three)  # dzielenie całkowite
print(five % three)

print(float('inf'))  # rzutowanie stringa z wartością
# inf (infinity) na float o wartości inf czyli infinity

print(float('inf') > 999999999999999999999999999)  # tutaj nam pokazuje
#  wynik rzutowania boolean true infinity jest większe od inta 999999......

print(-float('inf'))  # minus nieskończoność

#  Laboratory
name = 'Jurek'
name_01 = 'Chris'
age = 53
age_01 = 17
daysInYear = 365
message = '%s is %d years old, so is about %d days old.'
message_01 = '{0:s} is {1:d} years old, so is about {2:d} days old.'
message_03 = '{} is {} years old, so is about {} days old.'
print(message % (name, age, daysInYear * age))
print(message_01.format(name, age, daysInYear * age))
print(message_03.format(name_01, age_01, daysInYear * age_01))

number = 1234567890
divider = 12345

print('%d divided by %d is %d and the rest is %d' %
      (number, divider, number // divider, number % divider))
