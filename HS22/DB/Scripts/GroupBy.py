from .BaseOperand import BaseOperand

class GroupBy(BaseOperand):
    def __init__(self, header, column: str):
        super().__init__()
        self._header = header
        self._column = column
        
        if column not in header:
            raise Exception(f"Column {column} not present in header")
        
        
    def group_by(self, data, ascending: bool = True, log: bool = False):
        
        index = self._header.index(self._column)
        
        grouped = sorted(data, key=lambda x: x[index])
        
        if log:
            print(*self._header, sep='\t')
        
        if not ascending:
            grouped = grouped[::-1]
            
        return self.clean_data(grouped, log)
            
        