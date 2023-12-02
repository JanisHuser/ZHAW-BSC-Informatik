# Branching

## Comparison

```assembler

CMP{cond} Rn, Operand2      ; Rn - Operand2

CMN{cond} Rn, Operand2      ; Rn + Operand2

BEQ		equal			; (Rn-Operand2 == 0) 	equal 		(zero flag set)
BNE		not_equal		; (Rn-Operand2 != 0)	not equal	(zero flag not set)


equal
not_equal
higher
```


## Flag testing

```assembler
; test shifted register (if bit is set)
TST<c> <Rn>,#<const>        ; Rn & Const

BHI		higher			; (Rn & Const == Const)
BLO		lower			; (Rn & Const == 0)			zero flag set
```


TODO