# Table de tracabilite - Exigences / Tests / Code

## 1. Liste des exigences

Les exigences sont derivees des docstrings et du comportement attendu de chaque fonction
du module `calculatrice.py`.

| ID | Description |
|----|-------------|
| CALC-01 | L'utilisateur peut additionner deux nombres |
| CALC-02 | L'utilisateur peut soustraire deux nombres |
| CALC-03 | L'utilisateur peut multiplier deux nombres |
| CALC-04 | L'utilisateur peut diviser deux nombres (retourne None si diviseur = 0) |
| CALC-05 | L'utilisateur peut verifier si un nombre est pair |
| CALC-06 | L'utilisateur peut calculer la factorielle d'un entier (retourne None si negatif) |
| CALC-07 | L'utilisateur peut inverser une chaine de caracteres |
| CALC-08 | L'utilisateur peut verifier si une chaine est un palindrome (insensible a la casse et aux espaces) |
| CALC-09 | L'utilisateur peut obtenir le maximum d'une liste (retourne None si vide) |
| CALC-10 | L'utilisateur peut calculer la moyenne d'une liste (retourne 0 si vide) |

## 2. Table de tracabilite

| Exigence | Tests associes | Fonction testee |
|----------|---------------|-----------------|
| CALC-01 | test_addition_entiers_positifs, test_addition_entiers_negatifs, test_addition_positif_et_negatif, test_addition_flottants, test_addition_avec_zero, test_addition_grands_nombres | addition() |
| CALC-02 | test_soustraction_simple, test_soustraction_resultat_negatif, test_soustraction_negatifs, test_soustraction_zero, test_soustraction_memes_nombres | soustraction() |
| CALC-03 | test_multiplication_simple, test_multiplication_negatifs, test_multiplication_signe_mixte, test_multiplication_par_zero, test_multiplication_par_un, test_multiplication_flottants | multiplication() |
| CALC-04 | test_division_simple, test_division_resultat_decimal, test_division_negatifs, test_division_par_un, test_division_zero_par_nombre, test_division_par_zero, test_division_zero_par_zero | division() |
| CALC-05 | test_nombre_pair, test_nombre_impair, test_negatif_pair, test_negatif_impair, test_zero_est_pair, test_un_est_impair | est_pair() |
| CALC-06 | test_factorielle_cinq, test_factorielle_dix, test_factorielle_zero, test_factorielle_un, test_factorielle_negatif, test_factorielle_negatif_grand | factorielle() |
| CALC-07 | test_inversion_simple, test_inversion_phrase, test_inversion_chaine_vide, test_inversion_un_caractere, test_inversion_palindrome | inverser_chaine() |
| CALC-08 | test_palindrome_simple, test_non_palindrome, test_palindrome_avec_majuscules, test_palindrome_avec_espaces, test_palindrome_chaine_vide, test_palindrome_un_caractere | est_palindrome() |
| CALC-09 | test_maximum_simple, test_maximum_negatifs, test_maximum_mixte, test_maximum_un_element, test_maximum_doublons, test_maximum_liste_vide | maximum() |
| CALC-10 | test_moyenne_simple, test_moyenne_flottants, test_moyenne_negatifs, test_moyenne_un_element, test_moyenne_liste_vide | moyenne() |

## 3. Verification de la couverture des exigences

Toutes les exigences sont couvertes par au moins un test :

| Exigence | Couverte ? | Nb tests |
|----------|-----------|----------|
| CALC-01 | Oui | 6 |
| CALC-02 | Oui | 5 |
| CALC-03 | Oui | 6 |
| CALC-04 | Oui | 7 |
| CALC-05 | Oui | 6 |
| CALC-06 | Oui | 6 |
| CALC-07 | Oui | 5 |
| CALC-08 | Oui | 6 |
| CALC-09 | Oui | 6 |
| CALC-10 | Oui | 5 |

Total : 58 tests, 10 exigences couvertes sur 10.

## 4. Tracabilite dans le code

Chaque test contient un commentaire avec l'identifiant de l'exigence qu'il couvre.
Par exemple :

```python
def test_division_par_zero(self):
    # CALC-04 -- le code retourne None au lieu de lever une exception
    resultat = division(10, 0)
    assert resultat is None
```

Cela permet de naviguer dans les deux sens :
- **Descendant** : a partir d'une exigence (CALC-04), on retrouve tous les tests qui la couvrent
- **Ascendant** : a partir d'un test, on sait quelle exigence il valide grace au commentaire

## 5. Tests orphelins

Aucun test orphelin dans la suite actuelle. Chaque test est relie a une exigence.
