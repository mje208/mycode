#!/usr/bin/env/python3


challenge= ["science", "turbo", ["goggles", "eyes"], "nothing"]


trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]


nightmare= {"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}


# Challenge list
print(f' my {challenge[2][1]}! the {challenge[2][0]} do {challenge[3]}!')

# Trial list
a = trial[2].get('goggles')
b = trial[2].get('eyes')
c = trial[3]


print(f'my {a}! the {b} do {c}!')

# Nightmare list
a = nightmare['user']['name']['first']
b = nightmare['kumquat']
c = nightmare['d']

print(f'my {a}! the {b} do {c}!')

