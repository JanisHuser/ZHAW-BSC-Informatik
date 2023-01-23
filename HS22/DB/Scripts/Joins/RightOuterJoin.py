from .BaseJoin import BaseJoin
from .NaturalJoin import NaturalJoin

class RightOuterJoin(NaturalJoin):
    
    def __init__(self, header_A, header_B):
        super().__init__(header_A, header_B)
            
    def join(self, a, b, log: bool = False):
        
        if log:
            print ("Natural join on a and b")
        header, rows = super().join(a, b, log)
        
        if log:
            print()
             print("Apply right outer join")
            print (*header, sep='\t')
        
        if len(b) > 0:
            full_length = len(b[0]) if len(rows) is 0 else len(rows[0])
            
            to_extend = full_length - len(b[0])
        
            for row in b:
                
                if not self.is_used(row, rows, to_extend):
                    temp_row = []
                    for i in range(to_extend):
                        temp_row.append(None)
                    
                        
                    for cell in row:
                        temp_row.append(cell)
                    
                    rows.append(temp_row)
                
                
        return header, self.clean_data(rows, log)
            
        
    def is_used(self, row_b, rows, offset):
        for other_row in rows:
            used = True
            for i, cell in enumerate(row_b):
                if other_row[offset + i] is not cell:
                    used = False
                    break
                    
            if used:
                return True
                
        return False
            
            
                
            
        