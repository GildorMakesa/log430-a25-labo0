"""
Calculator app tests
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""

from calculator import Calculator

def test_app():
    my_calculator = Calculator()
    assert my_calculator.get_hello_message() == "== Calculatrice v1.0 =="

def test_addition_bug():
    my_calculator = Calculator()
    assert my_calculator.addition(2, 2) == 4

def test_subtraction():
    my_calculator = Calculator()
    assert my_calculator.subtraction(5, 3) == 2
    assert my_calculator.subtraction(3, 5) == -2
    assert my_calculator.subtraction(0, 0) == 0


def test_multiplication():
    my_calculator = Calculator()
    assert my_calculator.multiplication(3, 4) == 12
    assert my_calculator.multiplication(-2, 5) == -10
    assert my_calculator.multiplication(0, 99) == 0


def test_division():
    my_calculator = Calculator()
    assert my_calculator.division(10, 2) == 5
    assert my_calculator.division(9, 3) == 3
    assert my_calculator.division(5, 2) == 2.5


def test_division_by_zero():
    my_calculator = Calculator()
    assert my_calculator.division(5, 0) == "Erreur : division par zéro"
    assert my_calculator.last_result == "Error"  # Vérifie que l'état interne est mis à jour