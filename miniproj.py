#!/usr/bin/env/python3


import random

def users_choice()
    choices = [ 'rock', 'paper', 'scissors']
    dchoices = input('rock, paper, or scissors?\n').lower()
    while dchoices not in choices:
        dchoices = input('that is not one of the choices, please enter rock, paper, or scissors\n')
    return dchoices

def computer_choice()
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def winner(dchoices, 



