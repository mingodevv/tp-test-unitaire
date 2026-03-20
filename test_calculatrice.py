"""
Tests unitaires pour le module calculatrice.
Couvre les cas nominaux, les cas limites et les cas d'erreur
pour chaque fonction du module.
"""

import pytest
from calculatrice import (
    addition,
    soustraction,
    multiplication,
    division,
    est_pair,
    factorielle,
    inverser_chaine,
    est_palindrome,
    maximum,
    moyenne,
)

# ============================================================
# Tests addition
# ============================================================


class TestAddition:
    """Tests pour la fonction addition."""

    # --- cas nominaux ---

    def test_addition_entiers_positifs(self):
        # CALC-01
        assert addition(3, 5) == 8

    def test_addition_entiers_negatifs(self):
        # CALC-01
        assert addition(-4, -7) == -11

    def test_addition_positif_et_negatif(self):
        # CALC-01
        assert addition(10, -3) == 7

    def test_addition_flottants(self):
        # CALC-01
        assert addition(1.5, 2.3) == pytest.approx(3.8)

    # --- cas limites ---

    def test_addition_avec_zero(self):
        # CALC-01
        assert addition(0, 0) == 0
        assert addition(5, 0) == 5
        assert addition(0, -3) == -3

    def test_addition_grands_nombres(self):
        # CALC-01
        assert addition(10**18, 10**18) == 2 * 10**18


# ============================================================
# Tests soustraction
# ============================================================


class TestSoustraction:
    """Tests pour la fonction soustraction."""

    # --- cas nominaux ---

    def test_soustraction_simple(self):
        # CALC-02
        assert soustraction(10, 4) == 6

    def test_soustraction_resultat_negatif(self):
        # CALC-02
        assert soustraction(3, 8) == -5

    def test_soustraction_negatifs(self):
        # CALC-02
        assert soustraction(-5, -3) == -2

    # --- cas limites ---

    def test_soustraction_zero(self):
        # CALC-02
        assert soustraction(0, 0) == 0

    def test_soustraction_memes_nombres(self):
        # CALC-02
        assert soustraction(42, 42) == 0


# ============================================================
# Tests multiplication
# ============================================================


class TestMultiplication:
    """Tests pour la fonction multiplication."""

    # --- cas nominaux ---

    def test_multiplication_simple(self):
        # CALC-03
        assert multiplication(3, 4) == 12

    def test_multiplication_negatifs(self):
        # CALC-03
        assert multiplication(-2, -5) == 10

    def test_multiplication_signe_mixte(self):
        # CALC-03
        assert multiplication(-3, 7) == -21

    # --- cas limites ---

    def test_multiplication_par_zero(self):
        # CALC-03
        assert multiplication(100, 0) == 0
        assert multiplication(0, 0) == 0

    def test_multiplication_par_un(self):
        # CALC-03
        assert multiplication(7, 1) == 7

    def test_multiplication_flottants(self):
        # CALC-03
        assert multiplication(0.1, 0.2) == pytest.approx(0.02)


# ============================================================
# Tests division
# ============================================================


class TestDivision:
    """Tests pour la fonction division."""

    # --- cas nominaux ---

    def test_division_simple(self):
        # CALC-04
        assert division(10, 2) == 5.0

    def test_division_resultat_decimal(self):
        # CALC-04
        assert division(7, 2) == 3.5

    def test_division_negatifs(self):
        # CALC-04
        assert division(-10, 2) == -5.0

    # --- cas limites ---

    def test_division_par_un(self):
        # CALC-04
        assert division(9, 1) == 9.0

    def test_division_zero_par_nombre(self):
        # CALC-04
        assert division(0, 5) == 0.0

    # --- cas d'erreur ---

    def test_division_par_zero(self):
        # CALC-04 -- le code retourne None au lieu de lever une exception
        resultat = division(10, 0)
        assert resultat is None

    def test_division_zero_par_zero(self):
        # CALC-04
        assert division(0, 0) is None


# ============================================================
# Tests est_pair
# ============================================================


class TestEstPair:
    """Tests pour la fonction est_pair."""

    # --- cas nominaux ---

    def test_nombre_pair(self):
        # CALC-05
        assert est_pair(4) is True

    def test_nombre_impair(self):
        # CALC-05
        assert est_pair(7) is False

    def test_negatif_pair(self):
        # CALC-05
        assert est_pair(-6) is True

    def test_negatif_impair(self):
        # CALC-05
        assert est_pair(-3) is False

    # --- cas limites ---

    def test_zero_est_pair(self):
        # CALC-05
        assert est_pair(0) is True

    def test_un_est_impair(self):
        # CALC-05
        assert est_pair(1) is False


# ============================================================
# Tests factorielle
# ============================================================


class TestFactorielle:
    """Tests pour la fonction factorielle."""

    # --- cas nominaux ---

    def test_factorielle_cinq(self):
        # CALC-06
        assert factorielle(5) == 120

    def test_factorielle_dix(self):
        # CALC-06
        assert factorielle(10) == 3628800

    # --- cas limites ---

    def test_factorielle_zero(self):
        # CALC-06
        assert factorielle(0) == 1

    def test_factorielle_un(self):
        # CALC-06
        assert factorielle(1) == 1

    # --- cas d'erreur ---

    def test_factorielle_negatif(self):
        # CALC-06 -- retourne None pour un negatif
        assert factorielle(-1) is None

    def test_factorielle_negatif_grand(self):
        # CALC-06
        assert factorielle(-100) is None


# ============================================================
# Tests inverser_chaine
# ============================================================


class TestInverserChaine:
    """Tests pour la fonction inverser_chaine."""

    # --- cas nominaux ---

    def test_inversion_simple(self):
        # CALC-07
        assert inverser_chaine("bonjour") == "ruojnob"

    def test_inversion_phrase(self):
        # CALC-07
        assert inverser_chaine("hello world") == "dlrow olleh"

    # --- cas limites ---

    def test_inversion_chaine_vide(self):
        # CALC-07
        assert inverser_chaine("") == ""

    def test_inversion_un_caractere(self):
        # CALC-07
        assert inverser_chaine("a") == "a"

    def test_inversion_palindrome(self):
        # CALC-07
        assert inverser_chaine("aba") == "aba"


# ============================================================
# Tests est_palindrome
# ============================================================


class TestEstPalindrome:
    """Tests pour la fonction est_palindrome."""

    # --- cas nominaux ---

    def test_palindrome_simple(self):
        # CALC-08
        assert est_palindrome("kayak") is True

    def test_non_palindrome(self):
        # CALC-08
        assert est_palindrome("python") is False

    def test_palindrome_avec_majuscules(self):
        # CALC-08 -- la fonction ignore la casse
        assert est_palindrome("Kayak") is True

    def test_palindrome_avec_espaces(self):
        # CALC-08 -- la fonction ignore les espaces
        assert est_palindrome("esope reste ici et se repose") is True

    # --- cas limites ---

    def test_palindrome_chaine_vide(self):
        # CALC-08
        assert est_palindrome("") is True

    def test_palindrome_un_caractere(self):
        # CALC-08
        assert est_palindrome("x") is True


# ============================================================
# Tests maximum
# ============================================================


class TestMaximum:
    """Tests pour la fonction maximum."""

    # --- cas nominaux ---

    def test_maximum_simple(self):
        # CALC-09
        assert maximum([1, 5, 3, 9, 2]) == 9

    def test_maximum_negatifs(self):
        # CALC-09
        assert maximum([-10, -3, -7]) == -3

    def test_maximum_mixte(self):
        # CALC-09
        assert maximum([-5, 0, 5, 10]) == 10

    # --- cas limites ---

    def test_maximum_un_element(self):
        # CALC-09
        assert maximum([42]) == 42

    def test_maximum_doublons(self):
        # CALC-09
        assert maximum([7, 7, 7]) == 7

    # --- cas d'erreur ---

    def test_maximum_liste_vide(self):
        # CALC-09 -- retourne None pour une liste vide
        assert maximum([]) is None


# ============================================================
# Tests moyenne
# ============================================================


class TestMoyenne:
    """Tests pour la fonction moyenne."""

    # --- cas nominaux ---

    def test_moyenne_simple(self):
        # CALC-10
        assert moyenne([10, 20, 30]) == pytest.approx(20.0)

    def test_moyenne_flottants(self):
        # CALC-10
        assert moyenne([1.5, 2.5, 3.0]) == pytest.approx(2.333, rel=1e-2)

    def test_moyenne_negatifs(self):
        # CALC-10
        assert moyenne([-10, 10]) == pytest.approx(0.0)

    # --- cas limites ---

    def test_moyenne_un_element(self):
        # CALC-10
        assert moyenne([5]) == pytest.approx(5.0)

    # --- cas d'erreur ---

    def test_moyenne_liste_vide(self):
        # CALC-10 -- retourne 0 au lieu de lever une exception
        assert moyenne([]) == 0
