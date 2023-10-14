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