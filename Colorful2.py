import time
import os
from colorama import Fore, Style, init

init(autoreset=True)

# Homer Simpson face with open and closed eyes
open_eyes = """
{yellow}          _____
{yellow}        /       \\
{yellow}       /   ___   \\
{yellow}      /   /{reset}{white}0{yellow}  \\   \\
{yellow}     /   /|     |\\   \\
{yellow}    /   / |{reset}{white}0{yellow}  | \\   \\
{yellow}   /___/   |___|  \\___\\
"""

closed_eyes = """
{yellow}          _____
{yellow}        /       \\
{yellow}       /   ___   \\
{yellow}      /   /{reset}{white}-{yellow}  \\   \\
{yellow}     /   /|     |\\   \\
{yellow}    /   / |{reset}{white}-{yellow}  | \\   \\
{yellow}   /___/   |___|  \\___\\
"""


def print_homer(face):
    colored_face = face.format(
        yellow=Fore.YELLOW, white=Fore.WHITE, reset=Style.RESET_ALL
    )
    print(colored_face)


def animate_homer():
    os.system("cls" if os.name == "nt" else "clear")
    for _ in range(3):
        print_homer(open_eyes)
        time.sleep(1)
        os.system("cls" if os.name == "nt" else "clear")
        print_homer(closed_eyes)
        time.sleep(0.5)
        os.system("cls" if os.name == "nt" else "clear")


animate_homer()