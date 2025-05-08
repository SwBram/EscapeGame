from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, name: str, role: str):
        self.name = name
        self.role = role

    @abstractmethod
    def ShowInfo(self) -> str:
        return f"name: {self.name}, role: {self.role}"