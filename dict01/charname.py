#!/usr/bin/env/python3


marvelchars = {
'starlord':
{'real name': 'peter quill',
'powers': 'dance moves',
'archenemy': 'thanos'},

'mystique':
{'real name': 'raven darkholme',
'powers': 'shape shifter',
'archenemy': 'professor x'},

'hulk':
{'real name': 'bruce banner',
'powers': 'super strength', 
'archenemy': 'adrenaline'},
}

def main(): 
    
    char_name = input('what character would you like to choose?\n')
    
    char_stat = input('what stat would you like?\n')

    answer = marvelchars.get(char_name).get(char_stat)

    print(answer)

main()

