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
    # Ce test va échouer car 2 + 2 est 4, et non 5.
    assert my_calculator.addition(2, 2) == 4