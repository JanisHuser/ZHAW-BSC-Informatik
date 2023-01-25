from .BaseJoin import BaseJoin
from .Cartesian import CartesianJoin

from ..Select import Select

class ThetaJoin(BaseJoin):
    
    def __init__(self, header_a, header_b, name_A: str, name_B: str):
        super().__init__(header_a, header_b)
        
        self._name_A = name_A
        self._name_B = name_B

        
    def join(self, a, b, query: str, log: bool = False):
        
        if log:
            print ("Apply Cartesian Join")
        cartesian = CartesianJoin(self._header_A, self._header_B, self._name_A, self._name_B)
        cartesian.set_bag(self.is_bag)
        
        header, combined_data = cartesian.join(a, b, log)
        
        if log:
            print (f"\nExecute Query: \"{query}\"")
        select = Select(header, query)
        select.set_bag(self._is_bag)
        selected_data = select.do(combined_data, log)
        
        
        return header, self.clean_data(data, log)
