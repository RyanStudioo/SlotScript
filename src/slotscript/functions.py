from .parser import Parser
from .datatypes.Return import Return


class Functions:
    keywords = [
        "load", # loads a pre saved script
    ]

    @classmethod
    def route_function(cls, line:list[str]):
        if line[0] in cls.keywords:
            if line[0] == "load":
                return Return(return_type="replace", content=cls.load(line))
            return None


    @classmethod
    def load(cls, line: list[str]):
        file_path = line[1]
        with open(file_path, "r", encoding="utf-8") as file:
            script = file.read()

        return Parser.parse(script)