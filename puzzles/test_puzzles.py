import pytest
from riddle_puzzle import RiddlePuzzle
from code_lock_puzzle import CodeLockPuzzle
from puzzle import Puzzle



lijsthints1 = ['het is iets dat je kan zien', 'het is iets dat in objecten is', 'het is iets dat diep kan zijn']

def test_RiddlePuzzle():
    """Test of RiddlePuzzle."""
    riddle = RiddlePuzzle('Hoe meer je ervan wegneemt hoe groter het wordt', 'gat', lijsthints1)
    assert riddle.check_solution('gat') == True
    assert riddle.check_solution('hey') == False

lijsthints2 = ['het is simpel', 'je moet steeds 1 omhoog gaan']

def test_CodeLockPuzzle():
    """Test of CodeLockPuzzle"""
    code = CodeLockPuzzle('wat is de code? ', '1234', lijsthints2)
    assert code.check_solution('1234') == True 
    assert code.check_solution('0538') == False
    