class BaseJoin():
    
    def __init__(self, attributes_A, attributes_B):
         self._map_A = attributes_A
         self._map_B = attributes_B
         
         
         self._header_commons = self.get_common_headers()
         
    def get_common_headers(self):
        '''
        Returns the common header list of the two maps
        '''
        
        header_a = self._map_A
        header_b = self._map_B
        
        commons = []
        for i, k in enumerate(header_a):
            if k in header_b:
                commons.append((i, header_b.index(k)))
                
        return commons
        
    def join(self, a, b, log: bool = False):
        raise NotImplementedError()