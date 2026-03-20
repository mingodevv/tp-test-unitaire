# Plan de test - Module Calculatrice

## 1. Objectifs

Le but de cette campagne de tests est de verifier le bon fonctionnement de toutes les
fonctions du module `calculatrice.py`. On veut s'assurer que chaque fonction se comporte
correctement dans les cas normaux, mais aussi dans les cas limites et les cas d'erreur.

## 2. Perimetre

Le module contient 10 fonctions :
- `addition`, `soustraction`, `multiplication`, `division` (operations arithmetiques)
- `est_pair` (verification de parite)
- `factorielle` (calcul de factorielle)
- `inverser_chaine` (inversion de chaine)
- `est_palindrome` (detection de palindrome)
- `maximum` (maximum d'une liste)
- `moyenne` (moyenne d'une liste)

## 3. Types de tests

Pour chaque fonction, on couvre trois categories :
- **Cas nominaux** : utilisation normale avec des donnees classiques
- **Cas limites** : valeurs frontieres (0, chaine vide, liste a 1 element, etc.)
- **Cas d'erreur** : entrees invalides ou comportements discutables du code (division par zero qui retourne None, factorielle negative, etc.)

## 4. Outils utilises

- **pytest** pour l'execution des tests
- **pytest-cov** pour la couverture de code
- **flake8** pour le linting
- **black** pour le formatage
- **mypy** pour la verification de types
- **radon** pour la complexite cyclomatique

## 5. Plan de test detaille

| ID | Fonction | Description du test | Donnees d'entree | Resultat attendu | Type | Statut |
|----|----------|---------------------|-------------------|------------------|------|--------|
| T-01 | addition | Addition de deux entiers positifs | a=3, b=5 | 8 | Nominal | OK |
| T-02 | addition | Addition de deux entiers negatifs | a=-4, b=-7 | -11 | Nominal | OK |
| T-03 | addition | Addition positif + negatif | a=10, b=-3 | 7 | Nominal | OK |
| T-04 | addition | Addition de flottants | a=1.5, b=2.3 | 3.8 | Nominal | OK |
| T-05 | addition | Addition avec zero | a=0, b=0 | 0 | Limite | OK |
| T-06 | addition | Addition grands nombres | a=10^18, b=10^18 | 2*10^18 | Limite | OK |
| T-07 | soustraction | Soustraction simple | a=10, b=4 | 6 | Nominal | OK |
| T-08 | soustraction | Resultat negatif | a=3, b=8 | -5 | Nominal | OK |
| T-09 | soustraction | Deux negatifs | a=-5, b=-3 | -2 | Nominal | OK |
| T-10 | soustraction | Zero moins zero | a=0, b=0 | 0 | Limite | OK |
| T-11 | soustraction | Memes nombres | a=42, b=42 | 0 | Limite | OK |
| T-12 | multiplication | Multiplication simple | a=3, b=4 | 12 | Nominal | OK |
| T-13 | multiplication | Deux negatifs | a=-2, b=-5 | 10 | Nominal | OK |
| T-14 | multiplication | Signe mixte | a=-3, b=7 | -21 | Nominal | OK |
| T-15 | multiplication | Multiplication par zero | a=100, b=0 | 0 | Limite | OK |
| T-16 | multiplication | Multiplication par un | a=7, b=1 | 7 | Limite | OK |
| T-17 | multiplication | Flottants | a=0.1, b=0.2 | 0.02 | Nominal | OK |
| T-18 | division | Division simple | a=10, b=2 | 5.0 | Nominal | OK |
| T-19 | division | Resultat decimal | a=7, b=2 | 3.5 | Nominal | OK |
| T-20 | division | Division de negatifs | a=-10, b=2 | -5.0 | Nominal | OK |
| T-21 | division | Division par un | a=9, b=1 | 9.0 | Limite | OK |
| T-22 | division | Zero divise par un nombre | a=0, b=5 | 0.0 | Limite | OK |
| T-23 | division | Division par zero | a=10, b=0 | None | Erreur | OK |
| T-24 | division | Zero divise par zero | a=0, b=0 | None | Erreur | OK |
| T-25 | est_pair | Nombre pair | n=4 | True | Nominal | OK |
| T-26 | est_pair | Nombre impair | n=7 | False | Nominal | OK |
| T-27 | est_pair | Negatif pair | n=-6 | True | Nominal | OK |
| T-28 | est_pair | Negatif impair | n=-3 | False | Nominal | OK |
| T-29 | est_pair | Zero | n=0 | True | Limite | OK |
| T-30 | est_pair | Un | n=1 | False | Limite | OK |
| T-31 | factorielle | Factorielle de 5 | n=5 | 120 | Nominal | OK |
| T-32 | factorielle | Factorielle de 10 | n=10 | 3628800 | Nominal | OK |
| T-33 | factorielle | Factorielle de 0 | n=0 | 1 | Limite | OK |
| T-34 | factorielle | Factorielle de 1 | n=1 | 1 | Limite | OK |
| T-35 | factorielle | Nombre negatif | n=-1 | None | Erreur | OK |
| T-36 | factorielle | Grand nombre negatif | n=-100 | None | Erreur | OK |
| T-37 | inverser_chaine | Inversion simple | "bonjour" | "ruojnob" | Nominal | OK |
| T-38 | inverser_chaine | Inversion phrase | "hello world" | "dlrow olleh" | Nominal | OK |
| T-39 | inverser_chaine | Chaine vide | "" | "" | Limite | OK |
| T-40 | inverser_chaine | Un seul caractere | "a" | "a" | Limite | OK |
| T-41 | inverser_chaine | Chaine palindrome | "aba" | "aba" | Limite | OK |
| T-42 | est_palindrome | Palindrome simple | "kayak" | True | Nominal | OK |
| T-43 | est_palindrome | Non palindrome | "python" | False | Nominal | OK |
| T-44 | est_palindrome | Palindrome avec majuscules | "Kayak" | True | Nominal | OK |
| T-45 | est_palindrome | Palindrome avec espaces | "esope reste ici et se repose" | True | Nominal | OK |
| T-46 | est_palindrome | Chaine vide | "" | True | Limite | OK |
| T-47 | est_palindrome | Un caractere | "x" | True | Limite | OK |
| T-48 | maximum | Liste classique | [1,5,3,9,2] | 9 | Nominal | OK |
| T-49 | maximum | Liste de negatifs | [-10,-3,-7] | -3 | Nominal | OK |
| T-50 | maximum | Liste mixte | [-5,0,5,10] | 10 | Nominal | OK |
| T-51 | maximum | Un seul element | [42] | 42 | Limite | OK |
| T-52 | maximum | Tous identiques | [7,7,7] | 7 | Limite | OK |
| T-53 | maximum | Liste vide | [] | None | Erreur | OK |
| T-54 | moyenne | Moyenne simple | [10,20,30] | 20.0 | Nominal | OK |
| T-55 | moyenne | Moyenne de flottants | [1.5,2.5,3.0] | 2.333 | Nominal | OK |
| T-56 | moyenne | Moyenne negatifs et positifs | [-10,10] | 0.0 | Nominal | OK |
| T-57 | moyenne | Un seul element | [5] | 5.0 | Limite | OK |
| T-58 | moyenne | Liste vide | [] | 0 | Erreur | OK |

## 6. Remarques sur le code source

Quelques choix dans le code sont discutables et meritent d'etre signales :

- **division(a, 0) retourne None** : en general on attendrait plutot une exception (ZeroDivisionError). Le test verifie le comportement actuel mais c'est un choix de conception questionnable.
- **factorielle(n<0) retourne None** : meme remarque, une ValueError serait plus explicite.
- **moyenne([]) retourne 0** : retourner 0 pour une liste vide est trompeur, ca pourrait masquer un bug dans le code appelant. Une exception ou None serait preferable.
- **maximum([]) retourne None** : au moins ici c'est None, mais la encore une exception serait plus propre.

Ces comportements sont testes tels quels car c'est le code fourni, mais en conditions reelles il faudrait les corriger.
