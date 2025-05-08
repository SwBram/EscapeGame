from .puzzle import Puzzle

class CodeLockPuzzle(Puzzle):
    def check_solution(self, answer: str) -> bool:
        return answer.strip() == self.solution

    def get_hint(self) -> str:
        if self.hint_index < len(self.hints):
            hint = self.hints[self.hint_index]
            self.hint_index += 1
            return hint
        return "Geen hints meer beschikbaar."
