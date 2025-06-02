def bottle_Countdown(amount):

    while amount > 1:

        amount_next = amount - 1

        print(f'\n{amount} bottles of beer on the wall, {amount} bottles of beer.\n'
              f'Take one down and pass it around, {amount_next} bottle(s) of beer on the wall.')
        
        amount -= 1

    print(f'\n{amount} bottle of beer on the wall, {amount} bottle of beer.\n'
        f'Take one down and pass it around, {amount_next-1} bottle of beer on the wall.')
    
    print('\nTime to buy more bottles of beer.')