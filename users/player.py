from user import User

class Player(User):
    def __init__(self, name: str, hints_count: int, puzzles_solved: int):
        super().__init__(name, role="Player")
        self.hints_count = hints_count
        self.puzzles_solved = puzzles_solved

    def GetName(self) -> str:
        """Return the name of the player."""
        return self.name
    
    def GetHintsCount(self):
        """Return player's hints count."""
        return self.hints_count
    
    def GetPuzzelsSolved(self):
        """Return player's puzzles solved."""
        return self.puzzles_solved
    
    def GetRole(self):
        """Return player role."""
        return self.role
    
    def ShowInfo(self) -> str:
        """Show player info."""
        return f"name: {self.name}, Hints count: {self.hints_count}, Puzzles solved: {self.puzzles_solved}"