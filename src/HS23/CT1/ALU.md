# Alu

```python,editable
def has_carry(result, bit_limits):
    m = (1<<bit_limits)
    return result & m == m

def is_negative(result, bit_limits):
    m = (1<<(bit_limits-1))
    return result & m == m

def is_zero(result, bit_limits):
    m = 0
    for i in range(bit_limits):
        m += (1<<i)

    return (result & m) == 0

def has_overflow(result,a,b, bit_limits):
    msb = (1<<(bit_limits-1))
    
    msb_a = (msb & a) == msb
    msb_b = (msb & b) == msb

    if not msb_a and not msb_b:
        return True
    
    return msb_a == msb_b
    
def limit(v, bit_limits):
    m = 0
    for i in range(bit_limits):
        m += (1<<i)
        
    return v & m
def add(a,b, bit_limits):
    result = a+b
    
    return {
        "result": hex(limit(result, bit_limits)),
        "N": is_negative(result, bit_limits),
        "Z": is_zero(result, bit_limits),
        "C":  has_carry(result, bit_limits),
        "V": has_overflow(result, a, b, bit_limits)
    }

def subtract(a,b, bit_limits):


    result = a+((~b)+1)
    
    
    return {
        "result": hex(limit(result, bit_limits)),
        "N": is_negative(result, bit_limits),
        "Z": is_zero(result, bit_limits),
        "C": not has_carry(result, bit_limits),
        "V": not has_overflow(result, a, b, bit_limits)
    }
   
print ("Add")
print (add(0x82, 0x12,8))
print (add(0x34, 0x72,8))
print (add(0xc2, 0x87,8))
print (add(0xa3, 0x62,8))
print (add(0x67, 0x99,8))

print()
print ("Subtract")
print (subtract(0x82, 0x12,8))
print (subtract(0x34, 0x72,8))
print (subtract(0xc2, 0x87,8))
print (subtract(0xa3, 0x62,8))
print (subtract(0x67, 0x99,8))

```