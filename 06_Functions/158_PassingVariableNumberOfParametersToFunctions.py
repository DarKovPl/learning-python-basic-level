def do_action(action, parameter):
    print('action: ', action)
    print('parameter: ', parameter)
    return


do_action('buy', 'shoes')
print('------------------------------------------------------------')


def do_action_2(action, *parameter):
    print('action: ', action)
    print('parameter: ', parameter)
    for element in parameter:
        print('Element is', element)
    return


do_action_2('buy', 'shoes', 'socks', 't-shirt')
print('------------------------------------------------------------')


def do_action_3(action, what, **parameter):
    print('action: ', action)
    print('what: ', what)
    print('parameter: ', parameter)
    for element in parameter:
        print(element, '=', parameter[element])
    return


do_action_3('buy', 'shoes', size=45, colour='brown', type='sport')
print('------------------------------------------------------------')


#  Laboratory

def print_animal(*animal):
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

    for element in animal:

        if element == 'cat':
            print(cat)

        elif element == 'bear':
            print(bear)

        elif element == 'bat':
            print(bat)

        else:
            print('This is wrong parameter: %s.' % element,
                  'You must choice and input correct name of animal: cat, bear or bat')

    return


print_animal('cat')
print('------------------------------------------------------------')
print_animal('cat', 'bat', 'bear', 'bat')
print('------------------------------------------------------------')


def days_to_left_new_year_eve(**date_to_count):
    # This functions is for counting days left to New Year's Eve

    from datetime import datetime

    for date in date_to_count:
        input_date = datetime(*date_to_count[date])
        year_to_counting = datetime(year=date_to_count[date][0], month=12, day=31)
        days_to_left = year_to_counting - input_date
        print(days_to_left.days)
    return


days_to_left_new_year_eve(date=[2020, 6, 11], date_1=[2020, 7, 1])
print('------------------------------------------------------------')
