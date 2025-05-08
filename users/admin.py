from user import User

class Admin(User):
    def __init__(self, name: str, field: str, permissions: list):
        super().__init__(name, role="Admin")
        self.permissions = permissions

    def ShowInfo(self):
        return f"Admin: {self.name}, Permissions: {self.permissions}"

    def ResetGame(self):
        return "Game has been reset by Admin"