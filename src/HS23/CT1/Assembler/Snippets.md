# Assembler

Whenever a command ends with the letter "S", the flags are updated, and only low registers (R0 - R7) can be used.


## Load value from registers

### Load Byte value
```assembler
ADDR_DIP_SWITCH_7_0         EQU     0x60000200

LDR     R0, =ADDR_DIP_SWITCH_7_0 	; read dip switch address into r0
LDRB    R0, [R0]					; read dip switches 15 to 8 into r0
```

### Load half word value
```assembler
ADDR_DIP_SWITCH_7_0         EQU     0x60000200

LDR     R0, =ADDR_DIP_SWITCH_7_0 	; read dip switch address into r0
LDRH    R0, [R0]					; read dip switches 15 to 8 into r0
```

### Load signed byte
```assembler
ADDR_DIP_SWITCH_7_0         EQU     0x60000200

LDR     R0, =ADDR_DIP_SWITCH_7_0 	; read dip switch address into r0
LDRSB   R0, [R0]					; read dip switches 15 to 8 into r0
```


### Load signed half word
```assembler
ADDR_DIP_SWITCH_7_0         EQU     0x60000200

LDR     R0, =ADDR_DIP_SWITCH_7_0 	; read dip switch address into r0
LDRSH   R0, [R0]					; read dip switches 15 to 8 into r0
```
## Storing Value

### Store byte

```assembler
ADDR_LED_31_24              EQU     0x60000103

LDR     R6, =ADDR_LED_31_24 		; store led address in R6
STRB    R3, [R6] 					; display array_index
```

### Store halfword

```assembler
ADDR_SEG7_BIN   			EQU		0x60000114

LDR     R6, =ADDR_SEG7_BIN			; load address
STRH    R0, [r6, #0]				; Store Index and Value to SSD
```

## Moving Register

```assembler
MOV		R5, R1						; copy R1 into R5
```

## Type Casting

### Sign Extension (signed)

Extend word without changing value

```assembler
SXTB    R3, R7                     ; extend R7 into R3 (8 bit to 32 bit)
SXTH    R3, R7                     ; extend R7 into R3 (16 bit to 32 bit)
```

### Zero Extension (signed)

Extend word without changing value

```assembler
UXTB    R3, R7                     ; extend R7 into R3 (8 bit to 32 bit)
UXTH    R3, R7                     ; extend R7 into R3 (16 bit to 32 bit)
```

# Bitmanipulation

Flags

- Z = 1 if result = 0
- Z = 0 otherwise
- C and V unchanged


## ANDS - Bitwise AND

```assembler
ANDS <Rdn>, <Rdn>, <Rm>				; Rdn = Rdn & Rm
```

## BICS - Clear Bits

```assembler
BICS <Rdn>, <Rdn>, <Rm>				; Rdn = Rdn & !Rm
```

## EORS - Invert Bits

```assembler
EORS <Rdn>, <Rdn>, <Rm>				; Rdn = Rdn $ Rm
```

## MVNS - Bitwise Not

```assembler
MVNS <Rd>, <Rm>						; Rd = !Rm
```

## ORRS - Set Bits

```assembler
ORRS    <Rdn>, <Rdn>, <Rm>			; Rdn = Rdn # Rm
```

```assembler
MOVS	R2, #0x48
ORRS	R1, R1, R2					; R1 = R1 | R2
```

# Shift / Rotate Instructions

## Shift Left

Shift Rdn left by Rm\<7:0\> bits, fill with zeros

```assembler
LSLS <Rdn>, <Rdn>, <Rm>				; Rdn = Shift Rdn left by Rm\<7:0\> bits, fill with zeros
```

### Immediate

```assembler
LSLS <Rdn>, <Rdn>, #<imm5>				; Rdn = Shift Rdn left by <imm5> bits, fill with zeros
```

## Shift Right

Shift Rdn right by Rm\<7:0\> bits, fill with zeros

```assembler
LSRS <Rdn>, <Rdn>, <Rm>				; Rdn = Shift Rdn right by Rm\<7:0\> bits, fill with zeros
```

### Immediate

```assembler
LSRS <Rdn>, <Rdn>, #<imm5>				; Rdn = Shift Rdn right by <imm5> bits, fill with zeros
```

### Fill with MSB

```assembler
ASRS <Rdn>, <Rdn>, <Rm>				; Rdn = Shift Rdn right by Rm\<7:0\> bits, fill with MSB
```

## Rotate right

cyclic rotate right by Rm\<7:0\> bits

```assembler
RORS <Rdn>, <Rdn>, <Rm>				; Rdn = cyclic rotate right by Rm\<7:0\> bits
```


# Kontrollstrukturen

## Switch Case

```assembly

NR_CASES                EQU     0x2

jump_table      ; ordered table containing the labels of all cases
                ; STUDENTS: To be programmed 
				DCD		case_dark
				DCD 	case_add
				DCD		...


case_dark       
                LDR  R0, =0
                B    display_result  

case_add        
                ADDS R0, R0, R1
                B    display_result


                CMP	R2, #NR_CASES
				BHS	case_bright
				LSLS R2, #2		; * 4
				LDR R7,=jump_table
				LDR R7, [R7, R2]
				BX R7

```