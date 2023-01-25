from .BaseOperand import BaseOperand

class Projection(BaseOperand):
    def __init__(self, headers, columns, extensions = []):
        super().__init__()
        self._headers = headers
        self._columns = columns
        self._extensions = extensions
        
        for col in columns:
            if col not in headers:
                raise Exception(f"Die Spalte {col} existiert in Tabelle nicht!, Projektion kann nicht berechnet werden.")
    
    def do(self, data, log: bool = False):
        
        result = []
        
        columns = []
        keys = []
        for i, k in enumerate(self._headers):
            if k in self._columns:
                columns.append(i)
                keys.append(k)
            
        if len(self._extensions) > 0:
            for _, header in self._extensions:
                keys.append(header)
                
        if log:
            print(*keys, sep='\t')
                
        for row in data:
            new_row = []
            
            for i in columns:
                new_row.append(row[i])  
            
            for i, h in enumerate(self._headers):
                locals()[h] = row[i]
                
            for equation, header in self._extensions:
                value = eval(equation)
                
                new_row.append(value)
            
                
                
            result.append(new_row)
            
            
        return self.clean_data(result, log)
        
        
    def set_bag(self, enable: bool):
        self._is_bag = enable