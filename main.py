import colorama
import time
import os
from colorama import Fore, Back, Style

print(Fore.CYAN + """
===============================================================================================
________                           _____        .__  __  .__                    __  .__      
\_____  \ ______   ____   ____    /  _  \_______|__|/  |_|  |__   _____   _____/  |_|__| ____  
 /   |   \\____ \_/ __ \ /    \  /  /_\  \_  __ \  \   __\  |  \ /     \_/ __ \   __\  |/ ___\ 
/    |    \  |_> >  ___/|   |  \/    |    \  | \/  ||  | |   Y  \  Y Y  \  ___/|  | |  \  \___ 
\_______  /   __/ \___  >___|  /\____|__  /__|  |__||__| |___|  /__|_|  /\___  >__| |__|\___  > 
        \/|__|        \/     \/         \/                    \/      \/     \/             \/  
        
===============================================================================================
""")
time.sleep(1)
print(Fore.LIGHTGREEN_EX + "Welcome to OpenArithmetic! Input the first number to continue.")
time.sleep(1)
num1 = float(input(Fore.WHITE + "[>] "))
time.sleep(1)
print(Fore.YELLOW + "What will be the operand? (Operands are different, refer to w3schools.com if you don't understand.)")
time.sleep(1)
operand = input(Fore.WHITE + "[>] ")
time.sleep(1)
print(Fore.YELLOW + "What will be your last number?")
time.sleep(1)
num2 = float(input(Fore.WHITE + "[>] "))
time.sleep(1)

# Grabs all numbers and puts them in an 'if' statement

if operand == "+":
    ans1 = num1 + num2
    print(ans1)

elif operand == "-":
    ans2 = num1 - num2
    print(ans2)

elif operand == "/":
    ans3 = num1 / num2
    print(ans3)

elif operand == "*":
    ans4 = num1 * num2
    print(ans4)

elif operand != "*, /, -, +":
    print(Fore.RED + "Invalid operand!")
    time.sleep(1)
    os.system("clear")