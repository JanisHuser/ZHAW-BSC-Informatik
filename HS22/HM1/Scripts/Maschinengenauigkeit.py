from numbers import Number
import numpy as np

class Scientific():
    
    def __init__(self, x, precision):
        notation = np.format_float_scientific(x, precision = precision)
        number, exponent = notation.split('e')
        self._precission = precision

        number = float(number)
        number /= 10
        number = round(number, precision)
        
        exponent = int(exponent)
        exponent += 1

        self._mantisse = number
        self._exponent = exponent
        
    def get_mantisse(self):
        return self._mantisse
    
    def get_exponent(self):
        return self._exponent
    
    
    def align(self, exponent):
        diff = self._exponent - exponent
        if diff == 0:
            return
        self._exponent = exponent
        self._mantisse *= 10**diff
        

def calc_eps(B: Number, n: Number) -> Number:
    """
    B = Basis
    n = 
    Berechnet die obere Schranke
    """
    eps = 1/2
    eps * B**(1-n)
    
    return eps
    
def add(a: Number, b: Number, precision: Number) -> Number:
    '''
    Addiert die Zahlen mit einer Genauigkeit
    a: Erste Zahl
    b: Zweite Zahl
    precision: Genauigkeit
    Gibt die Addierte Zahl zurück
    '''
    a = Scientific(a, precision)
    b = Scientific(b, precision)
    
    max_exponent = max(a.get_exponent(), b.get_exponent())

    a.align(max_exponent)
    b.align(max_exponent)
    
    mantisse = a.get_mantisse() + b.get_mantisse()
    
    mantisse = round(mantisse, precision)
    
    return mantisse * 10**max_exponent

def multiply(a: Number, b: Number, precision: Number) -> Number:
    
    a = Scientific(a, precision)
    b = Scientific(b, precision)
    
    max_exponent = max(a.get_exponent(), b.get_exponent())

    a.align(max_exponent)
    b.align(max_exponent)
    
    mantisse = a.get_mantisse() * b.get_mantisse()
    
    number = Scientific(mantisse * 10**(max_exponent*2), max_exponent *2)
  
    return number.get_mantisse() * 10**(number.get_exponent())

    