# Practice_26

# Library
from os import system as sys
from termcolor2 import colored
from pyfiglet import figlet_format

# Clear Terminal
sys('clear')

# Intro
print(colored(figlet_format("Exercises Part 1"), color='cyan'))
print(colored('=====================================================================', color='red'))
print(colored('Question Number ===> 26', color='blue'))
print(colored('// Be Sure To Read The README File To See The Question //', color='blue'))
print('                                            ')

for i in range(1, 11):
    if i == 3:
        continue

    elif i == 7:
        continue

    else:
        print(f'Number ===> {i}')

# Finish
# Create By Moein Heshmati
