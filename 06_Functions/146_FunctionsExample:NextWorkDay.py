def give_working_day():
    # prints the nearest working day date
    from datetime import date
    from datetime import timedelta

    day = date.today()
    # day = date(2017, 9, 30)

    if day.weekday() == 5:
        working_day = day + timedelta(days=2)

    elif day.weekday() == 6:
        working_day = day + timedelta(days=1)

    else:
        working_day = day
    print('Working day for', day, 'is', working_day)
    return


give_working_day()
print('-----------------------------------------------------------')

#  Laboratory

def days_to_new_year_eve():
    # This functions is for counting days left to New Year's Eve
    from datetime import date

    days_to_left = date(2020, 12, 31) - date.today()
    print(days_to_left.days)

    return


days_to_new_year_eve()
