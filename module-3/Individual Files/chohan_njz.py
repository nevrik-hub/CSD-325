"""
Cho-Han, by Al Sweigart al@inventwithpython.com
Modified by: Nicholas Zankl
Date: August 30, 2026
Assignment: Module 3.2 - Brownfield + Flowcharts
Course: CSD-325

Description:
A traditional Japanese dice game modified to include custom prompt formatting,
a 12% house fee, and a 10 mon bonus for dice rolls totaling 2 or 7.
"""

import random, sys

JAPANESE_NUMBERS = {1: 'ICHI', 2: 'NI', 3: 'SAN',
                    4: 'SHI', 5: 'GO', 6: 'ROKU'}

# CHANGE 1: Updated introduction to inform player of the 10 mon bonus for rolls totaling 2 or 7.
print('''Cho-Han, by Al Sweigart al@inventwithpython.com

In this traditional Japanese dice game, two dice are rolled in a bamboo
cup by the dealer sitting on the floor. The player must guess if the
dice total to an even (cho) or odd (han) number.

NOTICE: If your dice roll total is 2 or 7, you receive a 10 mon bonus!
''')

purse = 5000
while True:  # Main game loop.
    # Place your bet:
    print('You have', purse, 'mon. How much do you bet? (or QUIT)')
    while True:
        # CHANGE 2: Updated input prompt from '> ' to initials prompt 'mss: '
        pot = input('mss: ')
        if pot.upper() == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        elif not pot.isdecimal():
            print('Please enter a number.')
        elif int(pot) > purse:
            print('You do not have enough to make that bet.')
        else:
            # This is a valid bet.
            pot = int(pot)  # Convert pot to an integer.
            break  # Exit the loop once a valid bet is placed.

    # Roll the dice.
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    print('The dealer swirls the cup and you hear the rattle of dice.')
    print('The dealer slams the cup on the floor, still covering the')
    print('dice and asks for your bet.')
    print()
    print('    CHO (even) or HAN (odd)?')

    # Let the player bet cho or han:
    while True:
        # CHANGE 2: Updated input prompt from '> ' to initials prompt 'mss: '
        bet = input('mss: ').upper()
        if bet != 'CHO' and bet != 'HAN':
            print('Please enter either "CHO" or "HAN".')
            continue
        else:
            break

    # Reveal the dice results:
    print('The dealer lifts the cup to reveal:')
    print('  ', JAPANESE_NUMBERS[dice1], '-', JAPANESE_NUMBERS[dice2])
    print('    ', dice1, '-', dice2)

    # Calculate total roll
    rollTotal = dice1 + dice2

    # CHANGE 3: Check for bonus roll of 2 or 7, notify user, and add 10 mon to purse.
    if rollTotal == 2 or rollTotal == 7:
        print(f'Bonus! The total roll was {rollTotal}. You received a 10 mon bonus!')
        purse += 10

    # Determine if the player won:
    rollIsEven = rollTotal % 2 == 0
    if rollIsEven:
        correctBet = 'CHO'
    else:
        correctBet = 'HAN'

    playerWon = bet == correctBet

    # Display the bet results:
    if playerWon:
        print('You won! You take', pot, 'mon.')
        purse = purse + pot  # Add the pot to player's purse.
        
        # CHANGE 4: Updated house percentage fee from 10% (pot // 10) to 12% (int(pot * 0.12)).
        houseFee = int(pot * 0.12)
        print('The house collects a', houseFee, 'mon fee.')
        purse = purse - houseFee  # Deduct 12% fee.
    else:
        purse = purse - pot  # Subtract the pot from player's purse.
        print('You lost!')

    # Check if the player has run out of money:
    if purse <= 0:
        print('You have run out of money!')
        print('Thanks for playing!')
        sys.exit()
