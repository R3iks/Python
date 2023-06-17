import time
import os
from colorama import Fore, Style, init

init(autoreset=True)


def print_colorful_text(text, colors):
    for color in colors:
        print(color + text, end="\r", flush=True)
        time.sleep(0.2)


text = "Welcome to the world of Python!"
colors = [
    Fore.RED,
    Fore.GREEN,
    Fore.YELLOW,
    Fore.BLUE,
    Fore.MAGENTA,
    Fore.CYAN,
    Fore.WHITE,
]

# Clear the terminal
os.system("cls" if os.name == "nt" else "clear")

# Repeat the animation 5 times
for _ in range(5):
    print_colorful_text(text, colors)

print(Style.RESET_ALL + text)