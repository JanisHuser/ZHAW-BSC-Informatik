
from .SetBase import SetBase

class SetUnion(SetBase):
    
    def __init__(self, header):
        super().__init__(header)
        
        
    def do(self, a, b, log: bool = False):
        results = list(a)
        
        
        if log:
            print (*self._header, sep='\t')
        
        for row in b:
            results.append(row)
        
        return self.clean_data(results, log)
                