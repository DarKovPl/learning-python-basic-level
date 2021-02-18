from datetime import date
from datetime import timedelta


def give_working_day(year=date.today().year,
                     month=date.today().month,
                     day=date.today().day):
    # prints the nearest working day date

    day = date(year, month, day)

    if day.weekday() == 5:
        working_day = day + timedelta(days=2)

    elif day.weekday() == 6:
        working_day = day + timedelta(days=1)

    else:
        working_day = day

    return working_day


next_working_day = give_working_day(2017, 9, 2)
print('Next working day is: %s' % next_working_day)
print('------------------------------------------------------------')
next_working_day = give_working_day()
print('Next working day after today is: %s' % next_working_day)
print('------------------------------------------------------------')
print('Next working day after today is', give_working_day())


#  Laboratory

def print_animal(animal=''):
    #  This functions is printing three ascii-art images

    cat = r'''
        |\---/|
        | o_o |
         \_^_/'''
    bear = r'''
        /  \.-"""-./  \
        \    -   -    /
         |   o   o   |
         \  .-'"'-.  /
          '-\__Y__/-'
             `---`'''
    bat = r'''
              /\                 /\
             / \'._   (\_/)   _.'/ \
            /_.''._'--('.')--'_.''._\
            | \_ / `;=/ " \=;` \ _/ |
             \/ `\__|`\___/`|__/`  \/
                     \(/|\)/       '''
    if animal == 'cat':
        print(cat)

    elif animal == 'bear':
        print(bear)

    elif animal == 'bat':
        print(bat)

    else:
        print("You didn't write anything in 'animal' functions, you must choice "
              "and input correct name of one animal: cat, bear or bat" if animal == ''
              else "This is wrong parameter: '%s'. You must choice and input correct "
                   "name of animal: cat, bear or bat" % animal)
        return False

    return True


print_animal('cat')
print('------------------------------------------------------------')
print_animal()
print('------------------------------------------------------------')
if print_animal('cat') is True:
    print('Animal true')
else:
    print('Animal False')
print('------------------------------------------------------------')


def days_to_left_new_year_eve(year=date.today().year, month=date.today().month,
                              day=date.today().day):
    # This functions is for counting days left to New Year's Eve

    from datetime import datetime

    input_date = datetime(year=year, month=month, day=day)
    year_to_counting = datetime(year=year, month=12, day=31)
    days_to_left = year_to_counting - input_date

    return days_to_left.days


print(days_to_left_new_year_eve())
