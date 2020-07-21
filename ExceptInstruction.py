import sys

tasks_per_person = 0

try:
    tasks = 32
    persons_string = input('How many persons are there in the team? ')
    persons = int(persons_string)

    tasks_per_person = tasks / persons

except ValueError as e:
    print('Sorry - you need to enter an integer number %s.' % e)

except ZeroDivisionError as e:
    print('Sorry - you need to enter value > 0. %s' % e)

except:
    print('Something went wrong.....', sys.exc_info()[0])

print("Every person should have around", tasks_per_person, ' tasks.')
