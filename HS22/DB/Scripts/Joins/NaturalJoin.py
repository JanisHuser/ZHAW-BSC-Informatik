from .BaseJoin import BaseJoin

class NaturalJoin(BaseJoin):
    
    def __init__(self, header_A, header_B):
        super().__init__(header_A, header_B)
        
      
    def get_rows_in_b(self, row_a, b):
        # Find identical values in table_b
        
        rows = []
        
        for row in b:
            match = True
            for i_a, i_b in self._header_commons:
                value_a = row_a[i_a]
                value_b = row[i_b]
                
                if value_a != value_b:
                    match = False
                    break
                    
            if match:
                rows.append(row)
                
        return rows
                
    def join(self, a, b, log: bool = False):
    
        results = []
        
        headers = list(self._map_A)
        for h in self._map_B:
            if h not in headers:
                headers.append(h)
                
        if log:  
            print (*headers, sep='\t')
        
        for row in a:
            matching_rows = self.get_rows_in_b(row, b)
            
            
            for r in matching_rows:
                row_copy = list(row)
                for i, h in enumerate(self._map_B):
                    if h not in self._map_A:
                        row_copy.append(r[i])
                    
                results.append(row_copy)
            
            
        return (headers, self.clean_data(data, log))
        #for rowA in a:
            
            
            
    