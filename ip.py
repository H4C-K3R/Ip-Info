import requests
import time
import os
import sys
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Clear screen
os.system('cls' if os.name == 'nt' else 'clear')

# Slow printing function
def slow_print(text, delay=0.08):
    for c in text:
        sys.stdout.write(Fore.YELLOW + c)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# Welcome message
slow_print("\n\n\n \t\t\tWelcome to IP to Information Tools")
time.sleep(0.5)
os.system('cls' if os.name == 'nt' else 'clear')

# Logo with colors
print(Fore.CYAN + """
 ___ ____     ___        __        __       _   _             
|_ _|  _ \   |_ _|       \ \      / /__  __| |_| |__   ___ _ __ 
 | || |_) |   | |   _____ \ \ /\ / / _ \/ _` | | '_ \ / _ \ '__|
 | ||  __/    | |  |_____| \ V  V /  __/ (_| | | | | |  __/ |   
|___|_|      |___|          \_/\_/ \___|\__,_|_|_| |_|\___|_|   

""" + Fore.GREEN + """
Auther : Showrab
Team   : STLP
Tools  : IP to Information
""")

# Input
ip = input(Fore.LIGHTMAGENTA_EX + "Enter your target IP: ")

# Get IP info
txt = requests.get(f"http://ip-api.com/json/{ip}").json()

# Show result
if txt['status'] == 'success':
    print(Fore.YELLOW + "\n--- IP Information ---\n")
    print(Fore.GREEN + f"IP Address : " + Fore.WHITE + f"{txt['query']}")
    print(Fore.GREEN + f"Country    : " + Fore.WHITE + f"{txt['country']}")
    print(Fore.GREEN + f"Code       : " + Fore.WHITE + f"{txt['countryCode']}")
    print(Fore.GREEN + f"Region     : " + Fore.WHITE + f"{txt['regionName']}")
    print(Fore.GREEN + f"City       : " + Fore.WHITE + f"{txt['city']}")
    print(Fore.GREEN + f"ZIP        : " + Fore.WHITE + f"{txt['zip']}")
    print(Fore.GREEN + f"Latitude   : " + Fore.WHITE + f"{txt['lat']}")
    print(Fore.GREEN + f"Longitude  : " + Fore.WHITE + f"{txt['lon']}")
    print(Fore.GREEN + f"Timezone   : " + Fore.WHITE + f"{txt['timezone']}")
    print(Fore.GREEN + f"ISP        : " + Fore.WHITE + f"{txt['isp']}")
    print(Fore.GREEN + f"Org        : " + Fore.WHITE + f"{txt['org']}")
    print(Fore.GREEN + f"AS         : " + Fore.WHITE + f"{txt['as']}")
else:
    print(Fore.RED + f"\nError: {txt.get('message')}")