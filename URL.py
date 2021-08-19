# import <
import time
from win10toast import ToastNotifier
import hashlib
import os
from time import sleep
from urllib.request import urlopen, Request
toaster = ToastNotifier()
import sys
# >

lol = """
Done by: Bobb3ll1 | Pientä mainostusta :)
-                      .       ___         __  _      __     _____  
-                     / V\    / _ \___ ___/ / | | /| / /__  / / _/     
-                   / `  /   / , _/ -_) _  /  | |/ |/ / _ \/ / _/   
-                  <<   |   /_/|_|\__/\_,_/   |__/|__/\___/_/_/      
-                  /    |
-                /      |      ___                     _        ___   _                       _  _                  
-              /        |     / _ \  _ __   ___  __ _ | | ___  |   \ (_) ___ __  ___  _ _  __| |(_) ___ ___ __ _    
-            /    \  \ /     | (_) || '  \ / -_)/ _` || |/ -_) | |) || |(_-</ _|/ _ \| '_|/ _` || |(_-<(_-</ _` | _ 
-           (      ) | |      \___/ |_|_|_|\___|\__, ||_|\___| |___/ |_|/__/\__|\___/|_|  \__,_||_|/__//__/\__,_|(_)
-   ________|   _/_  | |                        |___/                                                               
- <__________\______)\__)

"""
lol2 = """https://discord.gg/GyxGQNVjc2"""
lol3 = """Liity mukaan kasvavaan yhteisöön!"""

# Asetetaan URL <
urll = ('https://tietokettu.net/') # Laita vahdittava URL sulkujen ja heittomerkkien sisään 
url = Request(urll, 
              headers={'User-Agent': 'Mozilla/5.0'})
# >

response = urlopen(url).read()

currentHash = hashlib.sha224(response).hexdigest()
print("Päällä.")
toaster.show_toast("Päällä.",f"Vahtimassa {urll} | Done By: Bobb3ll1")
while True:
    try:
        os.system('cls||clear')
        print (lol)
        for line in lol2:
            sleep(1 / 40)
            sys.stdout.write(line)
            sys.stdout.flush()
        print (' ')
        for line in lol3:
            sleep(1 / 40)
            sys.stdout.write(line)
            sys.stdout.flush()
        response = urlopen(url).read()
        currentHash = hashlib.sha224(response).hexdigest()
        time.sleep(30)
        response = urlopen(url).read()
        newHash = hashlib.sha224(response).hexdigest()
        if newHash == currentHash:
            continue
        else:
            os.system('cls||clear')
            print (lol)
            print (lol2)
            print (f'Havaittiin muutoksia | {urll}')
            toaster.show_toast(f"{urll} tuli muutos!","Bobb3ll1#2004")
            response = urlopen(url).read()
            currentHash = hashlib.sha224(response).hexdigest()
            time.sleep(30)
            continue

    except Exception as e:
        print("Jokin meni pieleen :(")


