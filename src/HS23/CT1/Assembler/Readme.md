# Assembler

# Special Characters

| Charakter(s) | Meaning / Usage |
|--|--|
| # | Precedes a number (decimal 1234 or hex 0x1234) |
| \[ \] | Content in squared brackets is interpreted as address |
| = | Pseudo- Instruction: Assembler reserves space in literal pool to store the value following the "=" sign. The value located at that address is then loaded to the target address. |
| \{ \} | Enumeration, e.g. comma seperated list of registers to be pushed on stack / written to memory |
| ! | "increment after" in load/store multiple |
| , | Seperates operands |
| ; | Preceds a comment |
| Other | Characters at beginning of line (no leadnig blanks) are interpreted as label |


## Flags

| Flag | Meaning | Action | Operands |
|------|---------|--------|----------|
| Negative | MSB = 1 | N = 1 | signed |
| Zero | Result = 0 | Z = 1 | signed, unsigned |
| Carry | Carry | C = 1 | unsigned |
| Overflow | Overflow | V = 1 | signed |


**N:** Wenn MSB des Resultats =1 ist

**Z:** Wenn Resultat =0 ist

**C:** Wee

### Overflow

The overflow flag is thus set when the most significant bit (here considered the sign bit) is changed by adding two numbers with the same sign (or subtracting two numbers with opposite signs). Overflow cannot occur when the sign of two addition operands are different (or the sign of two subtraction operands are the same).



### Usage 

```assembler
MRS <Rd>, APSR          ; Rd = APSR
MSR APSR, <Rn>          ; APSR = Rn
```

### Calculation

Binäre Subtraktion

```
HEX:    0x82 - 0x12
BIN:    1000'0010 - 0001'0010

subtrahend invertieren
        1000'0010 - 1110'1101
    
subtrahend +1 
        1000'0010 - 1110'1110
    
Zahlen addieren
        1000'0010 +
        1110'1110
        ---------
       10111'0000
        ========= 




```