from abc import ABC, abstractmethod

class User(ABC):
    """
    Abstract class that gives a basic definition for all users. 

    Required methods:
    - ShowInfo(): Shows the user's info.
    """
    def __init__(self, name: str, role: str):
        self.name = name
        self.role = role

    @abstractmethod
    def ShowInfo(self) -> str:
        pass