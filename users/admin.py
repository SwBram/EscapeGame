from user import User

class Admin(User):
    """
    Concrete class that represents an admin.

    Inherits:
        User: Abstract class.

    Methods:
    - GetName(): Return the name of the user.
    - GetRole(): Return user role.
    - GetPermissions(): Returns permissions.
    - Resetgame(): Resets the game.
    """
    def __init__(self, name: str, permissions: list):
        super().__init__(name, role="Admin")
        self.permissions = permissions

    def GetRole(self) -> str:
        """Return user role."""
        return self.role

    def GetName(self) -> str:
        """Return the name of the user."""
        return self.name

    def GetPermissions(self):
        """Returns permissions."""
        return self.permissions

    def ResetGame(self):
        """Resets the game."""
        return "Game has been reset by Admin"
    
    def ShowInfo(self):
        return f"Admin: {self.name}, Permissions: {self.permissions}"