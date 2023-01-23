from .BaseJoin import BaseJoin


class CartesianJoin(BaseJoin):
    
    def __init__(self, header_a, header_b, name_A, name_B):
        super().__init__(header_a, header_b)
        
        self._name_A = name_A
        self._name_B = name_B
        

    def join(self, a, b, log: bool = False):
        
        
        header = []
        data = []
        
        def create_header(base, comp, name):
            for h in base:
                if h in comp:
                    header.append(f"{name}.{h}")
                else:
                    header.append(h)
                    
        create_header(self._map_A, self._map_B, self._name_A)
        create_header(self._map_B, self._map_A, self._name_B)
        
        if log:
            print(*header, sep='\t')
        
        for row_a in a:
            for row_b in b:
                combined = list(row_a)
                
                combined.extend(row_b)
                
                data.append(combined)
            
            
        return header, self.clean_data(data, log)