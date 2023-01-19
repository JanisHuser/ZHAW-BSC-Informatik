class TruthTable():
    
    def __init__(self, inputs):
        self._inputs = inputs
        self._len = len(inputs)
        
    def check(self, equation: str):
        
        count_of_inputs = len(self._inputs)
        
        current = ""
        for i in range(count_of_inputs):
            current += self._inputs[i]
            current += "\t"
            
        current += "Z"
        print (current)
        
        for i in range(2**count_of_inputs):
            current = ""
            for j in reversed(range(count_of_inputs)):
                pos = count_of_inputs - j -1
                
                boolean = (i>>j) & 0x01
                
                locals()[self._inputs[j]] = boolean
                current += str(boolean)
                current += "\t"
            
            result = eval(equation)
            current += ("1" if result else "0")
            
            print(current)
            
        