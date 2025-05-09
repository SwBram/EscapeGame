from user import User

class Player(User):
    def __init__(self, name: str, hints_count: int, puzzles_solved: int):
        super().__init__(name, role="Player")
        self.hints_count = hints_count
        self.puzzles_solved = puzzles_solved

    def ShowName(self) -> str:
        return self.name
    
    def ShowHintsCount(self):
        return self.hints_count
    
    def ShowPuzzelsSolved(self):
        return self.puzzles_solved
    
    def ShowRole(self):
        return self.role
    
    def ShowInfo(self) -> str:
        return f"name: {self.name}"