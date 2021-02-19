## Table of Contents
1. [General Info](#general-info)
2. [Technologies](#technologies)
3. [Code Examples](#code-examples)
## General Info
***
This repository shows the progress of learning Python programming.
## Screenshot
![Image text](https://www.python.org/static/community_logos/python-logo-master-v3-TM.png)
## Technologies
***
A list of technologies used within the project:
* [Python](https://www.python.org/downloads/release/python-360/): Version 3.6 
## Code Examples
***
Link to file: https://github.com/DarKowPl/learning-python-basic-level/blob/master/05_Types:AdvancedInformation/138_LoopsCardGameWar.py

Examples of code:

    
    '''python
    
    # War Card Game with "War" rule in game
    
    war_pile_player_1 = []
    war_pile_player_2 = []
    
    for colour in colours:
        for figure in figures:
            a_card = figure.copy()
            a_card.update(Colour=colour)
            all_cards.append(a_card)
    
    random.shuffle(all_cards)
    
    for card in range(len(all_cards)):
    
        if card % 2 == 0:
    
            player_1.append(all_cards[card])
    
        else:
            player_2.append(all_cards[card])
    
    while len(player_1) and len(player_2) >= 1:
    
        power_of_player_1_hand = 0
        power_of_player_2_hand = 0
    
        for compare_1 in range(len(player_1)):
            power_of_player_1_hand += player_1[compare_1].get('Power')
        print('Currently Player_1 deck power: %d' % power_of_player_1_hand)
    
        for compare_2 in range(len(player_2)):
            power_of_player_2_hand += player_2[compare_2].get('Power')
        print('\t', 'Currently Player_2 deck power: %d' % power_of_player_2_hand)
    
        if power_of_player_1_hand > power_of_player_2_hand:
            percent_scale_hand_player_1 = power_of_player_1_hand / \
                                          power_of_player_2_hand * 100 - 100
            print('Player_1 has stronger deck than Player_2 by {0:.2f}%'.format
                  (round(percent_scale_hand_player_1, 2)))
    
        elif power_of_player_1_hand < power_of_player_2_hand:
            percent_scale_hand_player_2 = power_of_player_2_hand / \
                                          power_of_player_1_hand * 100 - 100
            print('Player_2 has stronger deck than Player_1 by {0:.2f}%'.format
                  (round(percent_scale_hand_player_2, 2)))
    
        else:
            print('Both of players have the same power in their cards')
    
        print('\n')
    
        card_1.append(player_1.pop(0))
        card_2.append(player_2.pop(0))
    
        if card_1[0].get('Power') > card_2[0].get('Power'):
    
            player_1.insert(len(player_1), card_1.pop())
            player_1.insert(len(player_1), card_2.pop())
    
            if len(war_pile_player_1) and len(war_pile_player_2) > 0:
    
                for war_pile_element in range(len(war_pile_player_1)):
                    player_1.insert(len(player_1), war_pile_player_1.pop(0))
                    player_1.insert(len(player_1), war_pile_player_2.pop(0))
    
        elif card_1[0].get('Power') < card_2[0].get('Power'):
    
            player_2.insert(len(player_2), card_1.pop())
            player_2.insert(len(player_2), card_2.pop())
    
            if len(war_pile_player_1) and len(war_pile_player_2) > 0:
    
                for war_pile_element in range(len(war_pile_player_1)):
                    player_2.insert(len(player_2), war_pile_player_1.pop(0))
                    player_2.insert(len(player_2), war_pile_player_2.pop(0))
    
        else:
    
            print('Waaaarrrrrrr!!!!!!!!!!!!!!!')
            war_pile_player_1.append(card_1.pop(0))
            war_pile_player_2.append(card_2.pop(0))
    
            if len(player_1) and len(player_2) >= 1:
                war_pile_player_1.append(player_1.pop(0))
                war_pile_player_2.append(player_2.pop(0))
                amount_of_rounds -= 1
            else:
                break
    
        amount_of_rounds += 1
    
    if len(player_1) > len(player_2):
        power_of_player_2_hand = len(player_2)
        winner = 'Player_1'
    
    else:
        power_of_player_1_hand = len(player_1)
        winner = 'Player_2'
    
    print('Currently Player_1 deck power: %d' % power_of_player_1_hand)
    print('\t', 'Currently Player_2 deck power: %d' % power_of_player_2_hand)
    print('{0:s} won the game in {1:d} rounds'.format(winner, amount_of_rounds))
    ```
