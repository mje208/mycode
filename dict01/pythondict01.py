#!/usr/bin/env/python3



# Understanding dictionaries; {key: value, key:, value...}

def main():
    # runtime function

    switch = {'hostname': 'sw1' , 'ip': '10.0.1.1', 'version': '1.2', 'vendor': 'cisco'}


    print(switch)

    print(type(switch))

    print( switch['hostname'] )
    print (switch ['ip'])
    
    print ('First test - .get()' )
    print (switch.get('lynx'))

    print('Second test -.get()')
    print (switch.get('lynx', 'THE KEY IS IN ANOTHER CASTLE!'))

    print ('Third test - .get()')
    print(switch.get('version'))
    
    print ('Fourth test - .keys()')
    print ( switch.keys() ) 

    print ('Fifth test - .values()')
    print (switch.values())
    
    del switch['vendor']

    print('Seventh test - .pop()')
    print(switch.pop('version'))
    print( switch.keys())
    print (switch.values())

    print ('Eighth test - ADD a new value')
    switch['adminlogin'] = 'karl08'
    print (switch.keys())
    print (switch.values())

    print('Ninth test - ADD a new value')
    switch['password'] = 'qwerty'
    print (switch.keys())
    print (switch.values())




if __name__ == '__main__':
    main()

