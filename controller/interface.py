from os import system


class Interface:
    def __init__(self, commands: dict = {}):
        self.commands = commands

        self.currentMethod = {
            "func": "",
            "parameters": []
        }

    def commands(self, commands_dict):
        """
        allowedCommands will definie which functions the interface can operate. To do that you will pass a 'key' (the commands itself) and a 'value' (the function that will be perfomed).
        """
        self.commands = commands_dict
        return self.commands

    def addCommand(self, name, func):
        self.commands[name] = func
        return self.commands[name]

    def removeCommand():
        pass

    def showCommands(self):
        return print(list(self.commands.keys()))

    def listen(self):
        """
        Receive the command name and return the function associated to it without running it.
        """
        system('clear')
        command = str(input("Digite um comando: "))
        self.currentMethod["func"] = self.commands[command]["func"]

        numberOfParameters = self.commands[command]["parameters"]

        for parameter in range(numberOfParameters):
            parameter = str(input("> "))
            self.currentMethod["parameters"].append(parameter)

        return print(self.currentMethod["parameters"])

    def execute(self, command):
        """
        Run the command returned by the listen method.
        """

        return self.currentMethod["func"](*self.currentMethod["parameters"])

    def quit():
        pass
