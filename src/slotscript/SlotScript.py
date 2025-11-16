from .executor import Executor

class SlotScript:

    @classmethod
    def execute(cls, script: str):
        return Executor.execute(script)