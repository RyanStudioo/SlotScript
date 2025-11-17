import shlex

class Parser:

    @classmethod
    def _parse_line(cls, line: str):
        split_line = shlex.split(line.strip())
        return [i for i in split_line if i]

    @classmethod
    def parse(cls, script: str):
        lines = script.split("\n")
        parsed = [cls._parse_line(line) for line in lines]
        return [i for i in parsed if i]

