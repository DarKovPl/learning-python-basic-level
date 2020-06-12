def week_day_in_french(day_number):

    names = {
        0: 'lundi',
        1: 'mardi',
        2: 'mercredi',
        3: 'jeudi',
        4: 'vendredi',
        5: 'samedi',
        6: 'dimanche'
    }
    return names.get(day_number, 'error')


print(week_day_in_french(4))
print(week_day_in_french(0))
print(week_day_in_french(9))
