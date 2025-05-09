from abc import ABC, abstractmethod

class Component(ABC):
    def __init__(self):
        self.running: bool = False

    @abstractmethod
    def start(self) -> None:
        self.running = True
        print("Component gestart.")

    @abstractmethod
    def stop(self) -> None:
        self.running = False
        print("Component gestopt.")
