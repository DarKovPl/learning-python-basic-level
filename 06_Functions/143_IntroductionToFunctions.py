def print_hello():
    # This functions just prints hello
    print('Hello')
    return


print_hello()
print_hello()
print_hello()
print('-----------------------------------------------------------')


#  Laboratory

def print_cat():
    #  This functions prints a cat logo
    txt = r'''
    |\---/|
    | o_o |
     \_^_/'''
    print(txt)
    return


def print_bear():
    # This functions prints a bear logo
    txt = r'''
    /  \.-"""-./  \
    \    -   -    /
     |   o   o   |
     \  .-'"'-.  /
      '-\__Y__/-'
         `---`'''
    print(txt)
    return


def print_bat():
    # This functions prints a bat logo
    txt = r'''
      /\                 /\
     / \'._   (\_/)   _.'/ \
    /_.''._'--('.')--'_.''._\
    | \_ / `;=/ " \=;` \ _/ |
     \/ `\__|`\___/`|__/`  \/
             \(/|\)/       '''
    print(txt)
    return


def print_separating_line():
    # This functions prints a separating line
    print('-----------------------------------------------------------')
    return


print_cat()
print_separating_line()
print_bear()
print_separating_line()
print_bat()
