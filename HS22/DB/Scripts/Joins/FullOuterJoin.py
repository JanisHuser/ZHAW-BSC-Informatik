from .BaseJoin import BaseJoin
from .NaturalJoin import NaturalJoin

class FullOuterJoin(NaturalJoin):
    
    def __init__(self, header_A, header_B):
        super().__init__(header_A, header_B)
            
    def join(self, a, b, log: bool = False):
        
        if log:
            print ("Natural join on a and b")
        header, rows = super().join(a, b, log)
        
        if log:
            print()
            print("Apply full outer join")
            print (*header, sep='\t')
        
        # Extend Length B
        if len(b) > 0:
            full_length = len(b[0]) if len(rows) is 0 else len(rows[0])
            
            to_extend = full_length - len(b[0])
        
            for row in b:
                
                if not self.is_used_b(row, rows, to_extend):
                    temp_row = []
                    for i in range(to_extend):
                        temp_row.append(None)
                    
                        
                    for cell in row:
                        temp_row.append(cell)
                    
                    rows.append(temp_row)
        
        if len(a) > 0:
            full_length = len(a[0]) if len(rows) is 0 else len(rows[0])
            
            to_extend = full_length - len(a[0])
        
            for row in a:
                
                if not self.is_used_a(row, rows):
                    temp_row = list(row)
                    
                    
                    
                    for i in range(to_extend):
                        temp_row.append(None)
                    
                        rows.append(temp_row)  
                
        return header, self.clean_data(rows, log)
            
    def is_used_a(self, row_a, rows):
        for other_row in rows:
            used = True
            for i, cell in enumerate(row_a):
                if other_row[i] is not cell:
                    used = False
                    break
                    
            if used:
                return True
                
        return False
        
    def is_used_b(self, row_b, rows, offset):
        for other_row in rows:
            used = True
            for i, cell in enumerate(row_b):
                if other_row[offset + i] is not cell:
                    used = False
                    break
                    
            if used:
                return True
                
        return False
            
            
                
            
        