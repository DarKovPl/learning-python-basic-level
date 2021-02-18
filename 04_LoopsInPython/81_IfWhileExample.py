values = [10, 43, 12, 48, 12, 11, 18, 98, 57, 28, 19, 27, 49, 19, 74]
i = 0
maxLen = len(values) - 2

while i < maxLen:
    print(i, values[i], values[i + 1], values[i + 2])
    if values[i] < values[i + 1] < values[i + 2]:
        print('\tFound: ', values[i], values[i + 1], values[i + 2])
    i += 1
print('-----------------------------------------------------------')
# Laboratory
numbers = [8, 18, 2, 4, 16, 5, 25, 4, 22, 3, 3, 5, 3, 9, 81, 11]
iteration = 0
while iteration < len(numbers) - 1:
    print(iteration, numbers[iteration], numbers[iteration + 1])
    if numbers[iteration + 1] == numbers[iteration] ** 2:
        print('Found: ', numbers[iteration], numbers[iteration + 1])
    iteration += 1
print('-----------------------------------------------------------')
iteration = 0
while iteration < len(numbers) - 2:
    print(iteration, numbers[iteration], numbers[iteration + 1],
          numbers[iteration + 2])
    if (numbers[iteration] ** 2 == numbers[iteration + 1] and
            numbers[iteration + 1] ** 2 == numbers[iteration + 2]):
        print('Found: ', numbers[iteration], numbers[iteration + 1],
              numbers[iteration + 2])
    iteration += 1
print('-----------------------------------------------------------')
iteration = 0
texts = ['zero', 'one', 'two', 'three', 'four', 'five', 'six',
         'seven', 'eight', 'nine']
while iteration < len(texts):
    print(iteration, texts[iteration])
    if iteration == len(texts)-1:
        break
    elif len(texts[iteration]) == len(texts[iteration+1]):
        print('Found the same length: ', texts[iteration],
              texts[iteration + 1])
    iteration += 1
