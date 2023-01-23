class Select():
    def __init__(self, headers, selection: str):
        self._headers = headers
        self._selection = selection
        
        
    def do(self, data, log: bool = False):
        result = []
        
        if log:
            print(*self._headers, sep='\t')
        
        for row in data:
            for i, h in enumerate(self._headers):
                locals()[h] = row[i]
                
            if eval(self._selection):
                result.append(row)
                
                if log:
                    print (*row, sep='\t')
                
        return result
            
        