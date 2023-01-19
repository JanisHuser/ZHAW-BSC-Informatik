from numbers import Number
import numpy as np
def calc_err_abs(x, xr):
    '''
    Berechnet den absoluten Fehler von x und xr
    x: Korrektes Ergebnis
    xr: Fehlerhaftes Ergebnis
    '''
    return abs(xr - x)

    
def calc_err_rel(x, xr):
    '''
    Berechnet den relativen Fehler von x und xr
    x: Korrektes Ergebnis
    xr: Fehlerhaftes Ergebnis
    '''
    return abs((xr - x) / x)



class Scientific():
    
    def __init__(self, x, precision):
        notation = np.format_float_scientific(x, precision = precision)
        number, exponent = notation.split('e')
        self._precision = precision

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


    def get_value(self):
        mantisse = round(self._mantisse, self._precision)

        return (mantisse, self._exponent)

    def as_float(self):
        return self._mantisse * 10**self._exponent

        

def calc_eps(B: Number, n: Number) -> Number:
    """
    B = Basis
    n = 
    Berechnet die obere Schranke
    """
    eps = 1/2
    eps *= B**(1-n)
    
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
    # convert back to usable format
    return mantisse * 10**max_exponent

def multiply(a: Number, b: Number, precision: Number) -> Number:
    
    a = Scientific(a, precision)
    b = Scientific(b, precision)
    
    max_exponent = max(a.get_exponent(), b.get_exponent())

    a.align(max_exponent)
    b.align(max_exponent)
    
    mantisse = a.get_mantisse() * b.get_mantisse()
    
    number = Scientific(mantisse * 10**(max_exponent*2), max_exponent *2)
    # convert back to usable format
    return number.get_mantisse() * 10**(number.get_exponent())

    
# Stuff above needed for calculations

print("Aufgabe 1")

def a():
    x = 1.46
    
    precision = 3
    
    x_16 = multiply(x, 16, precision)
    
    res = multiply(x, x, precision)
    print("x^2","=",res)
    
    res = multiply(48, res, precision)
    print("48 * x^2","=", res)

    res = add(res, multiply(16, x, precision), precision)
    print("48*x^2 + 16x","=",res)
    
    res = add(res, -12, precision)
    print ("48*x^2 + 16x - 12","=", res)
    
    def exact():
        x_64 = np.float64(x)
        
        return 48 * (x_64**2) + 16*x_64 - 12
    print ("=============== RESULTAT ===============")
    print("Rechnerarithmetik", res)
    print("Numpy (exakt)", exact())
    
    print (f"absoluter Fehler: {calc_err_abs(exact(), res)}")
    print (f"relativer Fehler: {calc_err_rel(exact(), res)}")

    
def b():
    x = 1.46
    precision = 3
    
    res = multiply(48, x, precision)
    print ("48x", "=", res)
    
    res = add(res, 16, precision)
    print ("(48x + 16)", "=", res)
    
    res = multiply(res, x, precision)
    print ("(48x + 16)*x", "=", res)
    
    res = add(res, -12, precision)
    print("(48x + 16)*x -12", "=", res)
    
    def exact():
        x_64 = np.float64(x)
        return (48*x_64+16) *x_64 -12
            
    
    print("=============== RESULTAT ===============")
    print("Rechnerarithmetik", res)
    print("Numpy (exakt)", exact())

    print (f"absoluter Fehler: {calc_err_abs(exact(), res)}")
    print (f"relativer Fehler: {calc_err_rel(exact(), res)}")

        
    
print ("Teil a")
a()

print()
print ("Teil b")
b()

print("FESTSTELLUNG")
print("Mit dem Horner Schema ist der Absolute Fehler 1.3 fach kleiner")