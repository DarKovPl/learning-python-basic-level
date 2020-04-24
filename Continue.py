persons = ['Elizabeth', 'Steven@sales.mycompany.com', 'Sebastian',
           'Margaret', 'Svetlana@mycompany.eu', 'Raphael']
domain = 'mycompany.com'
emails = []

for person in persons:

    if '@' in person:
        emails.append(person)
    else:
        email = person+'@'+domain
        emails.append(email)
for email in emails:
    print(email)
print('-----------------------------------------------------------')

emails = []

for person in persons:

    if '@' in person:
        emails.append(person)
        continue

    email = person + '@' + domain
    emails.append(email)

for email in emails:
    print(email)
print('-----------------------------------------------------------')

menu = '''
Choose what you want me to do for you:
1 - COFFEE
2 - TEA
3 - MAKE ME SMILE
---------------
To stop this script select 0
'''

smile = '''

                          oooo$$$$$$$$$$$$oooo
                      oo$$$$$$$$$$$$$$$$$$$$$$$$o
                   oo$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o         o$   $$ o$
   o $ oo        o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o       $$ $$ $$o$
oo $ $ "$      o$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$o       $$$o$$o$
"$$$$$$o$     o$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$o    $$$$$$$$
  $$$$$$$    $$$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$$$$$$$$$$$$$$
  $$$$$$$$$$$$$$$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$$$$$$  """$$$
   "$$$""""$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     "$$$
    $$$   o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     "$$$o
   o$$"   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$       $$$o
   $$$    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$" "$$$$$$ooooo$$$$o
  o$$$oooo$$$$$  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$   o$$$$$$$$$$$$$$$$$
  $$$$$$$$"$$$$   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     $$$$""""""""
 """"       $$$$    "$$$$$$$$$$$$$$$$$$$$$$$$$$$$"      o$$$
            "$$$o     """$$$$$$$$$$$$$$$$$$"$$"         $$$
              $$$o          "$$""$$$$$$""""           o$$$
               $$$$o                                o$$$"
                "$$$$o      o$$$$$$o"$$$$o        o$$$$
                  "$$$$$oo     ""$$$$o$$$$$o   o$$$$""
                     ""$$$$$oooo  "$$$o$$$$$$$$$"""
                        ""$$$$$$$oo $$$$$$$$$$
                                """"$$$$$$$$$$$
                                    $$$$$$$$$$$$
                                     $$$$$$$$$$"
                                      "$$$""""
'''
while 1 > 0:

    print(menu)
    letter = int(input('What do you want select?:  '))

    if letter == 1:
        print('"Function COFFEE not implemented"')
        input(print('Please type enter to continue '))
        continue

    if letter == 2:
        print("Function TEA not implemented")
        input(print('Please type enter to continue '))
        continue

    if letter == 3:
        print(smile)
        input(print('Please type enter to continue '))
        continue

    if letter == 0:
        break

    else:
        input(print('"You need to make a valid choice. Press '
                    'ENTER and try again!"'))
