#!/usr/bin/env/python3


ipchk = input('apply an IP address: \n')

if ipchk == '192.168.70.1':
    print('looks like the IP address of the gateway was set: ' + ipchk + 'this is not recommended.')
elif ipchk:
    print('looks like the IP address was set: ' + ipchk)
else: 
    print('you did not provide input.')


