
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