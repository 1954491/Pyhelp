#!/usr/bin/env python3

"""
Programme pour afficher la documentation

Par Xavier Gagnon
"""
import sys
import colorama
from colorama import Fore, Style
colorama.init()

INITIALE = "XG"


def main() -> None:
    """Fonction principale"""

    print(Fore.YELLOW, f"[{INITIALE}]", end="")
    if len(sys.argv) != 2:
        print(Fore.RED, f"Le script s'attend a recevoir 1 argument, mais vous en avez frouni {len(sys.argv) - 1}")
        print(Fore.YELLOW,  f"USAGE: {sys.argv[0]} nombre", Fore.RESET)
        exit(1)

    
if __name__ == '__main__':
    main()