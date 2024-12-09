from time import sleep

r = ' '
while r != 0:
    try:
        r = int(input('Hello! Im thinking of a number that is neither negative nor positive,\n'
                            'can you guess what that number is?\n'
                            'R= '))

    except (ValueError, NameError):
        print("Came on, a tip: NOT is a float number, shall we try again?")
        sleep(.8)
        continue

    except KeyboardInterrupt:
        print('finishing program...')
        sleep(1)
        print('Bye!')
        break
    if r !=0:
        sleep(.8)
        print(f'f. Not is {r}, try again...')
    else:
        print('Very good, the only number that is not positive and negative is 0')
        sleep(1)
        print('Bye!')