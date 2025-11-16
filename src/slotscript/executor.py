from .parser import Parser
from .datatypes.Return import Return
from .functions import Functions


class Executor:

    @classmethod
    def execute(cls, script: str):
        parsed = Parser.parse(script)
        for idx in range(len(parsed)):
            line = parsed[idx]
            return_value = Functions.route_function(line)
            if not return_value: continue
            if return_value.return_type == "replace":
                parsed[idx:idx+1] = return_value.content
        print(parsed)

