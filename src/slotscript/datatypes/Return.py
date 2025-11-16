from typing import Literal, Any

class Return:
    def __init__(self, return_type: Literal["replace"], content: Any=None):
        self.return_type = return_type
        self.content = content
