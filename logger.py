from component import Component

class Logger(Component):
    def __init__(self):
        self.messages = []

    def add_message(self, message: str):
        self.messages.append(message)

    def get_messages(self) -> list[str]:
        return self.messages
    



    


