#!/usr/bin/env/python3


round = 0 
answer = ' '

while round < 3 and answer != 'brian':
    round += 1 
    answer = input('finish the movie title, "monty python\'s the life of ______":\n')
    if answer == 'brian':
        print('correct')
    elif round == 3: 
        print('sorry, the answer was brian.')
    elif answer == 'shrubbery':
        print('you gave the super secret answer!')
        break
    else: 
        print('sorry, try again.')

