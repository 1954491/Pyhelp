#!/usr/bin/env python3

"""
Programme pour afficher la documentation

Par Xavier Gagnon
"""
import sys as console
import colorama
import re
from colorama import Fore

colorama.init()

INITIALE = "XG"
REGEX_DE_COMMANDE_ACCEPTER = "\\w+\\.|\\w+"


def main() -> None:
    """Fonction principale"""

    print(Fore.YELLOW, f"[{INITIALE}]", Fore.RESET, end="", file=console.stderr)
    verifier_usage()
    verifier_arg()
    print("Affichage de l'aide pour", end="", file=console.stderr)
    print(Fore.MAGENTA, f"{console.argv[1]}", Fore.RESET, file=console.stderr)
    try:
        argument = ""
        if get_nombre_point(console.argv[1]):
            if console.argv[1][-1] == ".":
                argument = console.argv[1][:-1]
                exec(f"import {console.argv[1][:-1]}; {console.argv[1][:-1]}")
            else:
                exec(f"import {console.argv[1][:console.argv[1].find('.')]}; {console.argv[1]}")
                argument = console.argv[1]
        else:
            exec(console.argv[1])

        help(argument)
    except Exception as ex:
        print(Fore.YELLOW, f"[{INITIALE}]", Fore.RESET, end="", file=console.stderr)
        print(Fore.RED, ex, file=console.stderr)
        exit(1)


def get_nombre_point(commande) -> int:
    """Donne le nombre de point dans la commande"""
    nbpoint = 0
    for char in commande:
        if char == ".":
            nbpoint = nbpoint + 1
    return nbpoint


def verifier_usage() -> None:
    """Vérifier l'usage de la commande"""
    if len(console.argv) != 2:
        print(Fore.RED, f"Le script s'attend a recevoir 1 argument, mais vous en avez frouni {len(console.argv) - 1}")
        print(Fore.YELLOW, f"USAGE: {console.argv[0]} sujet", Fore.RESET)
        exit(1)


def verifier_arg() -> None:
    """Vérifie si la commande est accepter"""
    arg = list(re.finditer(REGEX_DE_COMMANDE_ACCEPTER, console.argv[1]))
    commande = ""
    for sequence in arg:
        commande += sequence.group()

    nbpoint = get_nombre_point(commande)

    if commande != console.argv[1] or 1 < len(arg) <= nbpoint:
        print(Fore.RED, "Le sujet de l'aide n'est pas valide:", end="", file=console.stderr)
        print(Fore.MAGENTA, F"{console.argv[1]}", Fore.RESET, file=console.stderr)
        exit(1)


if __name__ == '__main__':
    main()
