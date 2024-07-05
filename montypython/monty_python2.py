#!/usr/bin/env/python3


round = 0


while True: 

    round = round + 1
    print('finish the movie title, "monty python\'s the life of ______"')
    answer = input('your guess--> ')
    if answer == 'brian':
        print ('correct')
        break
    elif round==3:
        print('sorry, the answer was brian.')
        break
    else: 
        print('sorry, try again.')


