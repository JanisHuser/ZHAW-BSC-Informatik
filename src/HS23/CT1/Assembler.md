# Assembler

## Load value at registers

```assembler
ADDR_DIP_SWITCH_7_0         EQU     0x60000200

LDR		R0, =ADDR_DIP_SWITCH_7_0 	; read dip switch address into r0
LDR		R0, [R0]					; read dip switches 15 to 8 into r0
```

## Bitwise AND

```
ANDS	<Rd>, <Rt>, <Rm>			; store Rt & Rm into Rd
```