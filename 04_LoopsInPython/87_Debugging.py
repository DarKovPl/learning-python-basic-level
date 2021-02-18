cargo = [40, 20, 4, 5, 30, 8, 2, 7, 3, 19, 32, 40, 20, 35, 15, 32, 9]
cargo.sort()
cargo.reverse()
print('The cargo list is: ', cargo)

boxCapacity = 90
box = []
i = 0

while i < len(cargo) and (boxCapacity - sum(box) >= min(cargo)):
    if boxCapacity - sum(box) > cargo[i]:
        box.append(cargo[i])
    i += 1
print('The collected items sum is: ', sum(box))
print('The element are: ', box)
print('-------------------------------------------------------')

# Laboratory

number = 1
previous_number = 0

while number < 50:
    print(number + previous_number)
    previous_number = number
    number += 1
print('-------------------------------------------------------')
text = ''
number = 10
condition = True

while condition:
    text += 'x'
    print(text)

    if len(text) > number:
        condition = False
