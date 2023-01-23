from ..BaseOperand import BaseOperand

class SetBase(BaseOperand):
    def __init__(self, header):
        super().__init__()
        self._header = header

    def do(self, a, b, log: bool = False):
        raise NotImplementedError("Not supported")
        
    