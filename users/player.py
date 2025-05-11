from user import User

class Player(User):
    def __init__(self, name: str, hints_count: int, puzzles_solved: int):
        super().__init__(name, role="Player")
        self.hints_count = hints_count
        self.puzzles_solved = puzzles_solved

    def GetName(self) -> str:
        """Return the name of the user."""
        return self.name
    
    def GetHintsCount(self):
        """Return user's hints count."""
        return self.hints_count
    
    def GetPuzzlesSolved(self):
        """Return user's puzzles solved."""
        return self.puzzles_solved
    
    def GetRole(self):
        """Return user role."""
        return self.role
    
    def ShowInfo(self) -> str:
        """Show user info."""
        return f"name: {self.name}, Hints count: {self.hints_count}, Puzzles solved: {self.puzzles_solved}"