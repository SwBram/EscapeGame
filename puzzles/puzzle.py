from abc import ABC, abstractmethod
from typing import List
from typing import List
from riddle_puzzle import RiddlePuzzle
from code_lock_puzzle import CodeLockPuzzle



class Puzzle(ABC):
    def __init__(self, question: str, solution: str, hints: List[str]):
        self.question = question
        self.solution = solution
        self.hints = hints
        self.hint_index = 0

    @abstractmethod
    def check_solution(self, answer: str) -> bool:
        pass

    @abstractmethod
    def get_hint(self) -> str:
        pass



lijsthints_11 = ['het is iets dat je kan zien', 'het is iets dat in objecten is', 'het is iets dat diep kan zijn']
lijsthints_12 = ['het is iets dat je niet kan aanraken', 'het begint met een b']
lijsthints_21 = ['het is simpel', 'je moet steeds 1 omhoog gaan']
def getpuzzles():
    puzzles = [RiddlePuzzle('Hoe meer je ervan wegneemt hoe groter het wordt', 'gat', lijsthints_11, ), RiddlePuzzle('wat kan je breken zonder aan te raken', 'belofte', lijsthints_12), CodeLockPuzzle('wat is de code? ', '1234', lijsthints_21)]
    return puzzles