import pytest
from riddle_puzzle import RiddlePuzzle
from code_lock_puzzle import CodeLockPuzzle
from puzzle import Puzzle #niet nodig omdat je dat al geiport hebt in de andere files



lijsthints1 = ['het is iets dat je kan zien', 'het is iets dat in objecten is', 'het is iets dat diep kan zijn']

def test_RiddlePuzzle():
    """
    in de RiddlePuzzle
    test de methodes check_solution en get hint
    """
    riddle = RiddlePuzzle('Hoe meer je ervan wegneemt hoe groter het wordt', 'gat', lijsthints1)
    assert riddle.check_solution('gat') == True
    assert riddle.check_solution('hey') == False

    assert riddle.get_hint() == 'het is iets dat je kan zien'
    assert riddle.get_hint() == 'het is iets dat in objecten is'
    assert riddle.get_hint() == 'het is iets dat diep kan zijn'
    assert riddle.get_hint() == 'Geen hints meer beschikbaar.'

lijsthints2 = ['het is simpel', 'je moet steeds 1 omhoog gaan']

def test_CodeLockPuzzle():
    """in de CodeLockPuzzle
    test de methodes check_solution en get_hint"""
    code = CodeLockPuzzle('wat is de code? ', '1234', lijsthints2)
    assert code.check_solution('1234') == True 
    assert code.check_solution('0538') == False

    assert code.get_hint() == 'het is simpel'
    assert code.get_hint() == 'je moet steeds 1 omhoog gaan'
    assert code.get_hint() == 'Geen hints meer beschikbaar.'