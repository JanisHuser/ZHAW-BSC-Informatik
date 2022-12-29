from numbers import Number

def calc_iterative(xL: Number, xR: Number, tolerance: Number, log: bool = False):
    """
    Does the iterative approach
    Set log to true, to see each step
    Returns (n, xL, xR)
    """
    
    if log:
        print("n\txL\txR")
        
    
	while xR - xL > tol:
        xM = (xL + xR)/2
        yM = g(xM)
        
        if yM < 0:
            xL = xM
        else:
            xR = xM
    	    n = n + 1
            
        if log:
            print (f"{n}\t{xL}\t{xR}")
    
	return (n, xL, xR)