# -*- coding: utf-8 -*
#!/usr/bin/env python3
'''
i liked the idea of the script
so i edited the script for better optimization
if i had more time i will add more options
AKA : KTN / 0x666 | https://github.com/KTN1990
'''
from time import sleep
from random import choice
from string import digits, ascii_lowercase
from os import system as cmd
from platform import system as cos
if cos == 'Windows': cmd('cls') 
else:cmd('clear')

def kill_gen(domain,user,num,lent):
  for _ in range(num):
    rand_str = lambda n: ''.join([choice(ascii_lowercase+digits) for i in range(n)])
    print(f'\033[0;31m\033[1m EMAIL : {user}{rand_str(lent)}@{domain}')
    open('email.txt', 'a').write(f'{user}{rand_str(lent)}@{domain}\n')
logo = '''
\033[0;33m    I--------------I   
\033[0;33m    I--------------I          \033[0;31m   ██████╗ ██████╗ ██████╗  ██████╗███╗   ██╗ █████╗      ██╗  ██╗
\033[0;33m   .-'            '-.         \033[0;31m ██╔════╝██╔═══██╗██╔══██╗██╔═══██╗████╗  ██║██╔══██╗     ╚██╗██╔╝
\033[0;33m  / --.-.--,---,.--.,\        \033[0;31m ██║     ██║   ██║██████╔╝██║   ██║██╔██╗ ██║███████║█████╗╚███╔╝
\033[0;33m /--.-.--,---,.--.,-- \       \033[0;31m ██║     ██║   ██║██╔══██╗██║   ██║██║╚██╗██║██╔══██║╚════╝██╔██╗
\033[0;33m |--------------------|       \033[0;31m ╚██████╗╚██████╔╝██║  ██║╚██████╔╝██║ ╚████║██║  ██║     ██╔╝ ██╗
\033[0;33m |       OUR          |       \033[0;31m  ╚═════╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝     ╚═╝  ╚═╝
\033[0;33m |                    |
\033[0;33m |  SCRIPTS - LIKE    |                        \033[0;31m ███╗   ███╗ █████╗ ██╗██╗
\033[0;33m |                    |                        \033[0;31m ████╗ ████║██╔══██╗██║██║
\033[0;33m |     MEDICINE       |                        \033[0;31m ██╔████╔██║███████║██║██║
\033[0;33m |                    |                        \033[0;31m ██║╚██╔╝██║██╔══██║██║██║ 
\033[0;33m | [ Pharmacy Only ]  |                        \033[0;31m ██║ ╚═╝ ██║██║  ██║██║███████╗
\033[0;33m |____________________|                        \033[0;31m ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝
\033[0;33m |.,--.-.--,---,.--.-.|   
\033[0;33m |--.-.--,---,.--.,--.|
\033[0;33m '--------------------'                             
                                        \033[0;32m ╔--─────────────────────────────────--╗
                                        \033[0;32m |      [#] : Coded By Max-IQ          |
                                        \033[0;32m |                                     |
                                        \033[0;32m |      FB :facebook.com/GOV.iraq2     |
                                        \033[0;32m ╚--─────────────────────────────────--╝                                                                                                                   
'''                                                                                              
if __name__ == '__main__':
  try:
    print(logo)
    print('=========================================')
    domain = input('Write email domain here exm:(gmail.com)# ')
    user   = input('write The visible letters in email#  ')
    num    = int(input('Type number of email# '))
    lent   = int(input('How Much star in email# '))
    print('We start nOw')
    sleep(2)
    kill_gen(domain,user,num,lent)
    print('\033[0;0m')
  except Exception as e:
    print(e)
    exit(0)
