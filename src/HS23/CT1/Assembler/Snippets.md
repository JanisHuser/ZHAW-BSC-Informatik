# Assembler

## Load value from registers

### Load Byte value
```assembler
ADDR_DIP_SWITCH_7_0         EQU     0x60000200

LDR     R0, =ADDR_DIP_SWITCH_7_0 	; read dip switch address into r0
LDRB    R0, [R0]					; read dip switches 15 to 8 into r0
```

### Load half word value
```assembler
ADDR_DIP_SWITCH_7_0         EQU     0x60000200

LDR     R0, =ADDR_DIP_SWITCH_7_0 	; read dip switch address into r0
LDRH    R0, [R0]					; read dip switches 15 to 8 into r0
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

## Bitwise AND


Bitwise and between value and address
```assembler
BITMASK_LOWER_NIBBLE        EQU     0x0F

LDR		R2, =BITMASK_LOWER_NIBBLE	; read address of lower bitmask nibble
ANDS	R0, R0, R2					; store into r0 <- (r0 and mask: r2)
```


## Incrementing address

Increment R4 by one

```assembler
ADDS	R4, R4, #1					; increment register address
```

## Shift 

### Shift Left

```assembler
LSLS	R1, R1, #1					; increment index by multiplying it x2
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

## Bitmanipulation


### OR

```assembler
ORRS    R3, R7                     ; OR MASK
```

### CLR - Clear Bits

```assembler
BICS    R3, R7                     ; 
```

### XOR - Bitwise invert

```assembler
EORS    R3, R7                     ; 
```

### AND

```assembler
ANDS    R3, R7                     ; 
```

### Bits löschen

```assembler
ADDRESS      ECU     ...

LDR         R6, =ADDRESS        ; ADDRESSE in R6 laden
LDR         R1, [R6]            ; Wert von R6 in R1 laden
LDR         R2, =0x2220         ; Maske 0x2220 in R2 laden
BICS        R1, R2              ; Bits R2 in R1 löschen
STR         R1, [R6]            ; R1 in R6 schreiben
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