import random

my_numbers = []

while len(my_numbers) < 7:

    new_number = random.randint(1, 49)

    if new_number in my_numbers:
        print("Eliminated: ", new_number)
        continue

    my_numbers.append(new_number)

my_numbers.sort()
print("Those numbers will win: ", *my_numbers)

#  Laboratory

colours = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
figures = ['Ace', 'King', 'Queen', 'Jack', '10', '9']
all_cards = []
player_1 = []
player_2 = []

for figure in figures:
    for colour in colours:
        all_cards.append(figure + ' ' + colour)
random.shuffle(all_cards)

for card in range(len(all_cards)):

    if card % 2 == 0:
        player_1.append(all_cards[card])
    else:
        player_2.append(all_cards[card])

print(' Cards of Player 1 :', '; '.join([str(final_card) for final_card in player_1]),
      '\n', 'Cards of Player 2 :', '; '.join([str(final_card) for final_card in player_2]))
