persons = ['Elizabeth', 'Steven', 'Sebastian', 'Margaret', 'Svetlana',
           'Raphael']
domain = 'mycompany.com'

for person in persons:
    email = person + '@' + domain
    print('Email for\t', person, '\tis\t', email)
else:
    print('-- end of the list --')

# Laboratory

data = ['Error:File cannot be open',
        'Error:No free space on disk',
        'Error:File missing',
        'Warning:Internet connection lost',
        'Error:Access denied']

for eachElementInData in data:
    print(eachElementInData.upper())

print('------------------------------------------------------------')

elements = []

for eachElementInData in data:

    elements.extend(eachElementInData.split(':'))
    print(elements.pop(0).upper(), elements.pop(0))

print('-----------------------------------------------------------')

for eachElementInData in data:

    elements.extend(eachElementInData.split(':'))
    if elements[0] == 'Error':
        print(elements.pop(0), elements.pop().upper())
    else:
        print(elements.pop(0), elements.pop(0))
