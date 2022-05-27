# -*- coding: utf-8 -*-

import os
import time

def setup():
    while True:  
        print("""
        
             ╔═╗╔═╗╔═╗╔╗╔╦ ╦╔═╗╔═╗╔╦╗╦ ╦╔═╗╦═╗   ╔═╗╔═╗╦
             ║ ║╠═╝║╣ ║║║║║║║╣ ╠═╣ ║ ╠═╣║╣ ╠╦╝ ─ ╠═╣╠═╝║
             ╚═╝╩  ╚═╝╝╚╝╚╩╝╚═╝╩ ╩ ╩ ╩ ╩╚═╝╩╚═   ╩ ╩╩  ╩

                 [1] - Install Dependecies with PIP
                 [2] - Install Dependencies with PIP3
        """)

        _choice = str(input("╔═══[root@Zaqo]\n╚══ # "))

        if _choice == "1":
            print("[MODE - PIP] - Installing...")
            time.sleep(3)
            pip()
            break
        elif _choice == "2":
            print("[MODE - PIP3] - Installing...")
            time.sleep(3)
            pip3()
            break
        else:
            print("[ERROR] - Please choose one option.")
            time.sleep(2)
            os.system("clear")
            continue

def pip():
    os.system("pip install requests")
    os.system("pip install tkinter")
    os.system("pip install time")
    os.system("pip install os")
    os.system("pip install math")

def pip3():
    os.system("pip3 install requests")
    os.system("pip3 install tkinter")
    os.system("pip3 install time")
    os.system("pip3 install os")
    os.system("pip3 install math")

if __name__ == "__main__":
    setup()
