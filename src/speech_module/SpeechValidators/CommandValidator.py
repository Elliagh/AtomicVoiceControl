

class CommandValidator:

    def __init__(self, commands):
        self.commands = commands

    def find_command(self, command):
        if command in self.commands:
            return True
        else:
            return False