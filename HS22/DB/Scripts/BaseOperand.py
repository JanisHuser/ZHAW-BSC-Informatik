class BaseOperand():
    def __init__(self, is_bag: bool = False):
        self._is_bag = is_bag
        
        
    def set_bag(self, enable: bool) -> None:
        self._is_bag = enable
            
    
    def clean_data(self, data, log: bool = False): 
        '''
        Cleans the data from duplicates if not baggy
        '''
        
        
        if self._is_bag:
            
            for row in data:
                print (*row, sep='\t')    
            
            return data
            
        cleaned_data = []
        
        for row in data:
            if row not in cleaned_data:
                
                if log:
                    print(*row, sep='\t')
                cleaned_data.append(row)
                
                
        return cleaned_data
        