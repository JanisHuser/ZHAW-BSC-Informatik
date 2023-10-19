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