class Component:
    def __init__(self):
        self.running: bool = False

    def start(self) -> None:
        self.running = True
        print("Component gestart.")

    def stop(self) -> None:
        self.running = False
        print("Component gestopt")
