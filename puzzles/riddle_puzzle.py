from .puzzle import Puzzle

class RiddlePuzzle(Puzzle):
    def check_solution(self, answer: str) -> bool:
        return answer.strip().lower() == self.solution.lower()

    def get_hint(self) -> str:
        if self.hint_index < len(self.hints):
            hint = self.hints[self.hint_index]
            self.hint_index += 1
            return hint
        return "Geen hints meer beschikbaar."


