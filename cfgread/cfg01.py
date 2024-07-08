#!/usr/bin/env/python3


'''RZFeeser | Alta3 Research

Learning to read in files. This lab uses the following methods:

.read() - returns the file's contents as a string
.readlines() - returns the file's lines as a list
.seek() - moves the cursor around an open file '''

def main():

    configfile = open('vlanconfig.cfg', 'r')
    print (configfile.read())

    configfile.seek (0, 0)

    configlist = configfile.readlines()
    print(configlist)

    for x in configlist:
        print(x)
    
    configfile.close()

if __name__ == '__main__':
    main()

