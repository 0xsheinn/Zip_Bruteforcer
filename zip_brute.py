#!/usr/bin/python

import zipfile
from tqdm import tqdm
from termcolor import colored

print('''
 ██████╗ ██╗  ██╗███████╗██╗  ██╗ █████╗ 
██╔═████╗╚██╗██╔╝██╔════╝██║ ██╔╝██╔══██╗
██║██╔██║ ╚███╔╝ ███████╗█████╔╝ ███████║
████╔╝██║ ██╔██╗ ╚════██║██╔═██╗ ██╔══██║
╚██████╔╝██╔╝ ██╗███████║██║  ██╗██║  ██║
 ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝
                                         
 ''')

wordlist = input("[*] Enter your wordlist : ")
zip_file = input("[*] Enter your zip file : ")

zip_file = zipfile.ZipFile(zip_file)
n_words = len(list(open(wordlist, "rb")))

print(colored("\n\n[!] Bruteforcing......",'yellow'))
print("\n[*] Total Password : ", n_words)

with open(wordlist, "rb") as wordlist:
    for word in tqdm(wordlist, total=n_words, unit=" word"):
        try:
            zip_file.extractall(pwd=word.strip())
        except:
            continue
        else:
            print(colored("[+] Password found : " + word.decode().strip(),'green'))
            exit(0)

print(colored("\n\n[!] Password not found, try other wordlist.\n",'red'))
