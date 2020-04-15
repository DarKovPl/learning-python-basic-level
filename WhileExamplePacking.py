cargo = [40, 20, 4, 5, 30, 8, 2, 7, 3, 19, 32, 40, 20, 35, 15, 32, 9]
cargo.sort()
cargo.reverse()
print('The cargo list is: ', cargo)

boxCapacity = 90
box = []
i = 0

while i < len(cargo):  # and (boxCapacity - sum(box) >= min(cargo)):
    if boxCapacity - sum(box) > cargo[i]:
        box.append(cargo[i])
    i += 1
print('The collected items sum is: ', sum(box))
print('The element are: ', box)

# Laboratory
number = 1
previousNumber = 0

while number <= 50:
    print('%d + %d = %d' % (previousNumber, number,
                            (previousNumber + number)))
    number += 1
    previousNumber += 1

print('------------------------------------------------------------')
import random
my_number = random.randint(0, 20)
guess = -1
trials = []

print('Game: Guess my number')

while guess != my_number:

    guess = int(input('Type your number: '))
    trials.append(1)

    if guess == my_number:
        print('Congratulations, you guessed the number in '
              '{0:d} attempts.'.format(trials.count(1)))
        break
    else:
        print('The number is greater than your guess'
              if my_number > guess else 'The number '
                                        'is smaller than your guess')
        print('Try again.')
