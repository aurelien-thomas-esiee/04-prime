"""Retourne si un nombre est premier ou non"""
from math import sqrt

#### Fonction secondaire


def isprime(p):
    """une fonction secondaire qui vérifie si un entier est un nombre premier ou pas."""
    # votre code ici

    if p<=1:
        return False
    for i in range(2, int(sqrt(p)) + 1):
        if p % i == 0:
            return False
    return True

#### Fonction principale


def main():
    """la fonction principale qui fait appel à isprime et vérifie son bon fonctionnement"""

    # vos appels à la fonction secondaire ici

    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
