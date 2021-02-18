def give_working_day(year, month, day):
    # prints the nearest working day date
    from datetime import date
    from datetime import timedelta

    # day = date.today()
    day = date(year, month, day)

    if day.weekday() == 5:
        working_day = day + timedelta(days=2)

    elif day.weekday() == 6:
        working_day = day + timedelta(days=1)

    else:
        working_day = day
    print('Working day for', day, 'is', working_day)
    return


give_working_day(2017, 9, 30)
give_working_day(2017, 10, 1)
give_working_day(2017, 10, 2)
give_working_day(2017, 10, 3)
give_working_day(2017, 10, 4)
give_working_day(2017, 10, 5)
give_working_day(2017, 10, 6)

give_working_day(year=2017, month=12, day=6)
give_working_day(day=6, month=12, year=2018)
print('------------------------------------------------------------')


#  Laboratory

def print_animal(animal):
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
        print('Wrong parameter. You must choice and input correct name of '
              'animal: cat, bear or bat')
    return


print_animal('cat')
print('------------------------------------------------------------')


def days_to_left_new_year_eve(year, month, day):
    # This functions is for counting days left to New Year's Eve

    from datetime import datetime

    input_date = datetime(year=year, month=month, day=day)
    year_to_counting = datetime(year=year, month=12, day=31)
    days_to_left = year_to_counting - input_date
    print(days_to_left.days)

    return


days_to_left_new_year_eve(2012, 10, 20)
days_to_left_new_year_eve(month=5, day=2, year=2020)
days_to_left_new_year_eve(day=9, year=2020, month=6)
