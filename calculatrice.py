"""Module calculatrice -- fonctions utilitaires diverses."""


def addition(a, b):
    """Retourne la somme de deux nombres."""
    return a + b


def soustraction(a, b):
    """Retourne la difference entre deux nombres."""
    return a - b


def multiplication(a, b):
    """Retourne le produit de deux nombres."""
    return a * b


def division(a, b):
    """Retourne le quotient de deux nombres."""
    if b == 0:
        return None  # volontairement discutable
    return a / b


def est_pair(n):
    """Retourne True si le nombre est pair, sinon False."""
    return n % 2 == 0


def factorielle(n):
    """Calcule la factorielle d'un entier positif."""
    if n < 0:
        return None  # pas d'exception
    resultat = 1
    for i in range(1, n + 1):
        resultat *= i
    return resultat


def inverser_chaine(chaine):
    """Inverse une chaine de caracteres."""
    return chaine[::-1]


def est_palindrome(chaine):
    """Verifie si une chaine est un palindrome."""
    chaine = chaine.lower().replace(" ", "")
    return chaine == chaine[::-1]


def maximum(liste):
    """Retourne le maximum d'une liste."""
    if len(liste) == 0:
        return None  # comportement a discuter
    max_val = liste[0]
    for element in liste:
        if element > max_val:
            max_val = element
    return max_val


def moyenne(liste):
    """Retourne la moyenne d'une liste de nombres."""
    if len(liste) == 0:
        return 0  # choix discutable
    return sum(liste) / len(liste)
