
from .SetBase import SetBase

class SetSubtract(SetBase):
    
    def __init__(self, header):
        super().__init__(header)
        
        
    def do(self, a, b, log: bool = False):
        results = []
        
        
        if log:
            print (*self._header, sep='\t')
        
        for row in a:
            if row not in b:
                results.append(row)
                
        if log:
            for row in results:
                print(*row, sep='\t')
                
                
        return results
        