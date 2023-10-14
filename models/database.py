import os
import json


class Database:
    """
    This class is a singleton, in other words, it will always have only one instance at a time. Everytime you acess the object it will be the same in the whole application.
    """
    _instance = False

    def __new__(cls):
        if not cls._instance:  # Ou seja, se cls._instance == None
            cls._instance = super().__new__(cls)
        return cls._instance

    def set(self, arq):
        """
        Insert the json file name.
        """
        self.arq = f"{arq}.json"
        self.abs = os.path.abspath(arq)

    def create(self, key, value):
        """
        Add to json the data. The data is manipulated in the way [key, value].
        """
        with open(self.arq, 'r') as arq:
            data = json.loads(arq.read())
        
        data[key] = value

        with open(self.arq, 'w') as arq:
            json.dump(data, arq, indent=4)

        print('[CRIANDO UM NOVO ITEM NO BD]')

    def read(self, filter):
        """
        Read the json file. The filter can be "all", "keys" and "values".
        """
        with open(self.arq, "r") as arq:
            data = json.loads(arq.read())

            casos = {
                "all": data.items(),
                "keys": data.keys(),
                "values": data.values()
            }

            filtered = casos.get(filter)

            return filtered
        
    def update(self, data):
        print('[ATUALIZANDO UM ITEM NO BD]')

    def delete(self, data):
        print('[DELETANDO UM ITEM NO BD]')

    def execute(self, command, data=None):
        allowedFunctions = {
            "create": self.create,
            "read": self.read,
            "update": self.update,
            "delete": self.delete
        }

        if command not in allowedFunctions:
            print('Esse comando não existe')
            raise NotImplementedError

        return allowedFunctions[command](data)

    def __repr__(self):
        return f"<Database '{self.arq}'>"
