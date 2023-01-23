from .BaseOperand import BaseOperand

class Select(BaseOperand):
    def __init__(self, headers, selection: str):
        super().__init__()
        self._headers = headers
        self._selection = selection
        
        
    def do(self, data, log: bool = False):
        result = []
        
        if log:
            print(*self._headers, sep='\t')
        
            
        safe_headers = []
        selection = self._selection
        for h in self._headers:
            safe_header = h.replace('.', '_')
            safe_headers.append((h, safe_header))
            
            selection = selection.replace(h, safe_header)
            
            
        for row in data:
            for i, header in enumerate(safe_headers):
                h = header[1]
                locals()[h] = row[i]
                
            if eval(selection):
                result.append(row)
                
        return self.clean_data(result, log)
            
        