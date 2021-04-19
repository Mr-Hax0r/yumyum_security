from requests import get
from os import system
from sys import stdout
from time import sleep
from sys import exit
from platform import system as osname
import urllib
import re
from socket import gethostbyname
from subprocess import run
from json import loads
version = '1.0.0'

def clear():
    if osname == 'nt':
        system('cls')
    else:
        system('clear')


def banner():
    print('''
 __ __  __ __  ___ ___      __ __  __ __  ___ ___       _____   ___    __  __ __  ____   ____  ______  __ __ 
|  |  ||  |  ||   |   |    |  |  ||  |  ||   |   |     / ___/  /  _]  /  ]|  |  ||    \ |    ||      ||  |  |
|  |  ||  |  || _   _ |    |  |  ||  |  || _   _ |    (   \_  /  [_  /  / |  |  ||  D  ) |  | |      ||  |  |
|  ~  ||  |  ||  \_/  |    |  ~  ||  |  ||  \_/  |     \__  ||    _]/  /  |  |  ||    /  |  | |_|  |_||  ~  |
|___, ||  :  ||   |   |    |___, ||  :  ||   |   |     /  \ ||   [_/   \_ |  :  ||    \  |  |   |  |  |___, |
|     ||     ||   |   |    |     ||     ||   |   |     \    ||     \     ||     ||  .  \ |  |   |  |  |     |
|____/  \__,_||___|___|    |____/  \__,_||___|___|      \___||_____|\____| \__,_||__|\_||____|  |__|  |____/ 

''')
    print("""
    }--------------{+} Yum Yum Securty {+}--------------{
    }--------{+}  GitHub.com/............. {+}--------{
    \n""")

def main():
    while True:
        print('    [*]  Choose one of the options below  [*]\n')
        sleep(0.3)
        print('    [1]  Admin Page Finder \n')
        sleep(0.1)
        print('    [2]  Subdomain Finder \n')
        sleep(0.1)
        print('    [3]  Locataion Finder \n')
        sleep(0.1)
        print('    [4]  CMS Detection \n')
        sleep(0.1)
        print('    [5]  OS Detection  \n')
        sleep(0.1)
        print('    [6]  Shell Finder \n')
        sleep(0.1)
        print('    [7]  Port Scaner \n')
        sleep(0.1)
        print('    [8]  IP Finder \n')
        sleep(0.1)
        print('    [9]  Auto Updater  \n')  
        sleep(0.1)
        print('    [0]  Exit ...  \n') 

        choose = input('Yum~# ')

        if choose == '1':
            ssite = input('\n    [*]  please enter site example (https://site.com): ')
            if ssite[-1] != '/':
                ssite = ssite + '/'
            with open ('admin.txt', 'r') as f :
                line = f.read().splitlines()

            for i in line :
                check_site = ssite + i
                fiend_somting(check_site, 'admin')
            x = input('[*]    Back To Menu ? (Y/n) ')
            if x == 'y' or x == '':
                clear()
                banner()
            else:
                exit()

        elif choose == '2':
            ssite = input('\n    [*]  please enter site example (site.com): ')
            list_sub = finder_subdomain(ssite)
            print('{*}======================================{*}')
            for i in list_sub:
                print('     [+] '+i)
            print('{*}======================================{*}\n')
            x = input('[*]    Back To Menu ? (Y/n) ')
            if x == 'y' or x == '':
                clear()
                banner()
            else:
                exit()
        elif choose == '3':
            slowprint('coming soon')
        elif choose == '4':
            ssite = input('\n    [*]  please enter site example (site.com): ')
            res_cms = fiend_cms(ssite)
            print('\n{*}======================================{*}')
            print('[*]    CMS Detection : {}'.format(res_cms))
            print('{*}======================================{*}\n')
        elif choose == '5':
            ssite = input('\n    [*]  please enter site example (site.com): ')
            res = find_ttl(ssite)
            if res == 'linux':
                print('\n{*}======================================{*}')
                print('[*]    OS Detection : Linux')
                print('{*}======================================{*}\n')
            elif res == 'win':
                print('\n{*}======================================{*}')
                print('[*]    OS Detection : Windows')
                print('{*}======================================{*}\n')
            else:
                print('\n{*}======================================{*}')
                print('[*]    OS Detection : Unknow\n')
                print('{*}======================================{*}\n')
            x = input('[*]    Back To Menu ? (Y/n) ')
            if x == 'y' or x == '':
                clear()
                banner()
            else:
                exit()

        elif choose == '6':
            with open('shell.txt', 'r') as a :
                lines = a.read().splitlines()
            ssite = input('\n    [*]  please enter site example (https://site.com): ')
            if ssite[1] != '/':
                ssite = ssite + '/'

            for i in lines:
                check_site = ssite + i
                fiend_somting(check_site, 'shell')
            x = input('[*]    Back To Menu ? (Y/n) ')
            if x == 'y' or x == '':
                clear()
                banner()
            else:
                exit()
        elif choose == '7':
            slowprint('coming soon')


        elif choose == '8':
            print('eneter nuber one for fiend with subdomain or with api')
            chooseip = int(input('wich one you want ? 1 for sub 2 for api : '))
            if chooseip == 1:
                ssite = input('\n    [*]  please enter site example (site.com): ')
                print('{*}======================================{*}')
                fiend_ip_with_sub(ssite)
                print('{*}======================================{*}\n')
                x = input('[*]    Back To Menu ? (Y/n) ')
                if x == 'y' or x == '':
                    clear()
                    banner()
                else:
                    exit()
            elif chooseip == 2:
                slowprint('coming soon')
                x = input('[*]    Back To Menu ? (Y/n) ')
                if x == 'y' or x == '':
                    clear()
                    banner()
                

        elif choose == '9':
            auto_update()
        elif choose == '0':
            exit()
        else:
            pass


def slowprint(s):
    for c in s + '\n':
        stdout.write(c)
        stdout.flush()
        sleep(10. / 100)


class color:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    RESET = '\033[39m'
    BLACK = '\033[40m'
    RED = '\033[41m'
    GREEN = '\033[42m'
    YELLOW = '\033[43m'
    BLUE = '\033[44m'
    MAGENTA = '\033[45m'
    CYAN = '\033[46m'
    WHITE = '\033[47m'
    RESET = '\033[49m'

def fiend_somting(site, idk):
    try :
        openurl = urllib.request.urlopen(site)
        print('----------------------')
        print(color.GREEN + f"{idk} found >>> " + site)
        print("----------------------")
    except :
        print (f"{idk} not found >>> " + site)


def fiend_cms(site):
    if site[1] != '/':
        site = site + '/'
    r = get(site)
    source1 = r.text
    if 'WordPrees' in source1:
        return ('wordprees')
        check_cms_done = True
    if 'joomla' in source1:
        check_cms_done = True
        return ('joomla')
    if 'Drupal' in source1:
        check_cms_done = True
        return ('Drupal')
    if 'Modx' in source1:
        check_cms_done = True
        return ('Modx')
    if 'Bitrix' in source1:
        check_cms_done = True
        return ('Bitrix')
    if 'Opencart' in source1:
        check_cms_done = True
        return ('Opencart')
    else:
        check_cms_done = False
    if check_cms_done == False:
        try:
            r = get(f'{site}/robot.txt')
            source = r.text
            if 'WordPrees' in source:
                return ('wordprees')
                check_cms_done = True
            if 'joomla' in source:
                check_cms_done = True
                return ('joomla')
            if 'Drupal' in source:
                check_cms_done = True
                return ('Drupal')
            if 'Modx' in source:
                check_cms_done = True
                return ('Modx')
            if 'Bitrix' in source:
                check_cms_done = True
                return ('Bitrix')
            if 'Opencart' in source:
                check_cms_done = True
                return ('Opencart')

            else:
                check_cms_done = False
            if check_cms_done == False:
                pass
        except:
            check_cms_done = False
            pass


def find_ttl(site):
    host = gethostbyname(site)

    response_ping = run(['ping', '-c', '1', host], capture_output=True, timeout=2)

    response = re.search(r'ttl=([0-9]+)', str(response_ping)).group(1)

    if int(response) >= 100:
        return 'linux'
    elif int(response) < 100:
        return 'win'
    else:
        pass


def finder_subdomain(domain):
    clear()

    def crt_find():
        request = get("https://crt.sh/?q={}&output=json".format(domain))

        res_json = loads(request.text)

        list_res = []

        for num in range(0, len(res_json)):
            ress = res_json[num]['name_value'].splitlines()

            for num in range(0, len(ress)):
                if '*' not in ress[num]:
                    list_res.append(ress[num])
                    res = []
                    for i in list_res:
                        if i not in res:       
                            res.append(i)
                    response_crt = []        
                    for i in res:
                        if i[:4] == 'www.':
                            pass
                        else:
                            response_crt.append(i)       


        return response_crt

    return crt_find()

def auto_update():
    print(version)
    system('git pull origin main')

def fiend_ip_with_sub(site):
    site_lis = finder_subdomain(site)
    banner()
    for i in site_lis :
        sleep(2)
        try:
            print(f'[ {i} ]   --->  [ {gethostbyname(i)} ]')
        except:
            print(f'[ {i} ]   --->  [ Error ! ]')


banner()
main()
