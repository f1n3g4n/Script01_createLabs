#!/usr/bin/python3
# Created by F1neg4n

import os

path = '/home/' + os.getlogin() + '/labs'

def welcome():
    welc = 'SSH Connect'
    info = '[INFO] Python script to create SSH connections'
    os.system('clear')
    print(welc + '\n' + '*' * len(welc))
    print(info + '\n' + '-' * len(info))
    return

def newLabName():
    welcome()
    try:
        nameLab = input('[+] Enter the Lab name: ')
        while(nameLab == ''):
            nameLab = input('[+] Please, enter the Lab name: ')
    except(KeyboardInterrupt):
        os.system('clear')
        welcome()
        print('[-] Interrupted by user!')
        exit()
    return nameLab

def createFolders():
    nameLab = newLabName()
    print('[+] Creating work environment "' + nameLab + '"...')
    if(os.path.exists(path + '/' + nameLab + '/') == False):
        os.system('mkdir ' + nameLab)
        os.chdir(nameLab + '/')
        os.system('mkdir 1.-Content 2.-Exploits 3.-NMAP')
        print('[+] Done, Work environment succefully created!')
    else:
        print('[-] Sorry but "' + nameLab + '" already exists')
        exit()
    return

def createEnvironment():
    if(os.path.exists(path) == True):
        os.chdir(path)
        createFolders()
    else:
        os.system('mkdir ' + path)
        os.system('cd labs/')
        createFolders()
    return

if __name__ == '__main__':
    createEnvironment()
