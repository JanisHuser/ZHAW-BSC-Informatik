# Arithmetic Operations

| Mnemonic | Insruction | Function |
|--|--|--|
| ADD /ADDS | Addition | A + B |
| ADCS | Addiction with carry | A + B + c |
| ADR | Address to register | PC + A |
| SUB / SUBS | Subtraction | A - B |
| SBCS | Subtraction with carry (borrow) | A - B - NOT(c) |
| RSBS | Reverse Subtract (negative) | -1 * A |
| MULS | Multiplication | A * B |

## Add Instruction


### Update flags

- Update of Flags
- Result and two operands
- Only low registers

```assembler
ADDS <Rd>, <Rn>, <Rm>       ; Rd = Rn + Rm
```

### Dont update flags

- No update of flags
- High and low registers
- Rdn contains result and operand


```assembler
ADD <Rdn>, <Rm>             ; Rdn = Rdn + Rm
```


### Multi-Word Addition

```assembelr
ADCS <Rdn>, <Rm>
Rdn = Rdn + Rm + C
```

### Immediate (3 bytes)

- Update of flags
- Two different low registers and immediate value 0-7

```assembler
ADDS <Rd>,<Rn>, #<imm3>     ; Rd = Rn + <imm3>
```

### Intermediate (8 bytes)

- Update of flags
- Low register with intermediate value 0-255d
- Rdn stores result and operation

```assembler
ADDS <Rdn>, <#imm8>         ; Rdn = Rdn + <imm8>
```


# Negative Zahlen

$$
-a = 0 -a 
$$

## 2er Komplement

```assembler
RSBS <Rd>, <Rn>, #0
Rd = 0 - Rn
```

## Subtraction

```assembler
SUBS <Rd>, <Rn>, <Rm>       ; Rd = Rn - Rm
                            ;    = Rn + NOT(Rm) + 1
```

## Mutli-Word Arithmetic

```assembler
ADCS <Rdn>, <Rm>            ; Rdn = Rdn + Rm + C
SBCS <Rdb>, <Rm>            ; Rdn = Rdn - Rm - NOT(C)
                            ;     = Rdn + NOT(Rm) + C
```

## Multiplication

```assembler
MULS <Rdm>, <Rn>, <Rdm>     ; Rdm = Rn + Rdm
```


# Application Program Status Register (APSR)

Die vordersten 4 Bit (31 - 28) stehen für (N Z C V).

Nur Instruktionen die mit "S" enden beinflussen die Flags. Diese werden nach jeder Operation gesetzt.

| Flag | Meaning | Action | Operands |
|------|---------|--------|----------|
| Negative | MSB = 1 | N = 1 | signed |
| Zero | Result = 0 | Z = 1 | signed, unsigned |
| Carry | Carry | C = 1 | unsigned |
| Overflow | Overflow | V = 1 | signed | 

## APSR Lesen

```assembler
MRS <Rd>, APSR
```

## APSR schreiben

```assembler
MSR APSR, <Rn>
```

## Manual Multiplication

Multiply 10 x 12

1. Komplexere Zahl in Register R0 laden (12)
2. Einfachere Zahl in 2er Kompotenzen aufteilen (10 => 8+2 => $2^3 + 2^1$ )
3. R1 = R0 << 3
4. R2 = R0 << 1
5. R0 = R1 + R2

```assembler

MOVS R0, #12
LSLS R1, R0, #3
LSLS R2, R0, #1
ADDS R0, R1, R2

```

## Sign Casting

### Extension

#### Unsigned Extension

Bei der Extension, werden Nullen vor dem MSB hinzugefügt
```
1011 -> 0000 1011
0011 -> 0000 0011
```

#### Signed Extension

Bei der Extension, wird der Wert des MSB vor dem MSB hinzugefügt

```
1011 -> 1111 1011
0011 -> 0000 0011
```

### Truncation

Die Linken Ziffern werden abgeschnitten.