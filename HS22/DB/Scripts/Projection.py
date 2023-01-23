
class Projection():
    def __init__(self, headers, columns):
        self._headers = headers
        self._columns = columns
        
        
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
                
                
        if log:
            print(*keys, sep='\t')
                
        for row in data:
            new_row = []
            
            for i in columns:
                new_row.append(row[i])
                
            if log:
                print(*new_row, sep='\t')
            result.append(new_row)
            
        return result