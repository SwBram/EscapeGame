from abc import ABC, abstractmethod
from typing import List

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
