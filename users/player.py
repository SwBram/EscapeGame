from user import User

class Player(User):
    def __init__(self, name: str, hints_count: int, puzzles_solved: int):
        super().__init__(name, role="Player")
        self.hints_count = hints_count
        self.puzzles_solved = puzzles_solved

    def ShowInfo(self):
        return f"Player: {self.name}, Hints: {self.hints_count}, Puzzles Solved: {self.puzzles_solved}"

    def GetStatus(self):
        return f"Status: {self.puzzles_solved} puzzles solved, {self.hints_count} hints used"