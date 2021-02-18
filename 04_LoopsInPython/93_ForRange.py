for number in range(1, 21):

    if number % 2 == 0:
        print('Number %2d is %s' % (number, 'even'))
    else:
        print('Number %2d is %s' % (number, 'odd'))
print('----------------------------------------------------------')

# Laboratory

string_A = '+---+---+---+---+'
string_B = '|   |   |   |   |'

for A in range(10):
    print(string_A, '\tLoop: %d' % (A + 1))

print('----------------------------------------------------------')

for A in range(5):
    print(string_A, '\tMain loop: %d' % A)

    if A == 4:
        break
    for B in range(1):
        print(string_B)

print('-----------------------------------------------------------')

for X in range(1, 10):
    print('x' * X)

print('-----------------------------------------------------------')

for O in range(1, 10):

    if O % 2 == 1:
        print('O' * O)
    else:
        print('X' * O)
print('-----------------------------------------------------------')

for O in range(1, 10, 2):
    print('O' * O)

    if O == 9:
        break

    for X in range(1):
        print('x' * (O+1))
print('-----------------------------------------------------------')

# Rozwiązanie od Rafała z kursu do 2 Laba
for A in range(5):
    print(string_A, '\tMain loop: %d' % A)

    if A != 4:
        print(string_B)