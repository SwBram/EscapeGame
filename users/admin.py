from user import User

class Admin(User):
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
        return "Game has been reset by Admin"
    
    def ShowInfo(self):
        return f"Admin: {self.name}, Permissions: {self.permissions}"