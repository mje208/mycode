#!/usr/bin/env/python3


favcolor = input('what is your favorite color? \n')


if favcolor == 'blue' or favcolor == 'red' or favcolor == 'green':
    print('that is a great color choice. truly inspiring!\n')

elif favcolor == 'purple' or favcolor == 'pink' or favcolor == 'burgundy' or favcolor == 'orange':
    print('this is a hideous colors. try again.')

elif favcolor in ['1','2','3','4','5','6']:
    print('that is not a color, you silly goose.')

else:
    print('that is not a good color. you will now be swatted')


