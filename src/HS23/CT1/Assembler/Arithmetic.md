# Arithmetic Operations

## Add Instruction


### Register

- Update of Flags
- Result and two operands
- Only low registers

```assembler
ADDS <Rd>, <Rn>, <Rm>       ; Rd = Rn + Rm
```

### Register

- No update of flags
- High of low registers
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
