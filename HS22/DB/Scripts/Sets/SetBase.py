
class SetBase():
    def __init__(self, header):
        self._header = header

    def do(self, a, b, log: bool = False):
        raise NotImplementedError("Not supported")