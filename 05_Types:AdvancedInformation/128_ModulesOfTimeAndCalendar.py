import time
import calendar

print("Current time is... unix epoch: ", time.time())
print("Current time is... tuple: ", time.localtime(time.time()))
print("Current time is... for human: ", time.asctime(time.localtime(time.time())))
print("Current time is... for human: ", time.localtime(time.clock()))
print("\n\n\n")

print('--------------------------------------------------------')
print(calendar.month(2020, 5, w=5, l=2))
print('--------------------------------------------------------')
print(calendar.month(2020, 6))
print('--------------------------------------------------------')
print('week day is: ', calendar.weekday(2020, 5, 28))
print('--------------------------------------------------------')
calendar.setfirstweekday(6)  # funkcja wpływa tylko na wyświetlanie calendar
print('--------------------------------------------------------')
print(calendar.month(2020, 6))
print('--------------------------------------------------------')
print('week day is: ', calendar.weekday(2020, 5, 28))
print('--------------------------------------------------------')
print(' is 2020 a leap year? ', calendar.isleap(2020))
print('--------------------------------------------------------')
print('Leap days 2000-2017', calendar.leapdays(2000, 2017))
print('Leap days 2000-2020', calendar.leapdays(2000, 2020))
print('Leap days 2000-2021', calendar.leapdays(2000, 2021))

print(calendar.calendar(2018))
print('--------------------------------------------------------')

#  Laboratory

print(time.time())
print(time.localtime(time.time()))
print(calendar.month(1987, 3))
calendar.setfirstweekday(6)
print(calendar.month(1987, 3))
print(calendar.isleap(2000))
print(calendar.calendar(2019))
