# Memory

## Directives

### REQUIRE8
specifies that the current file requires 8-byte alignment of the stack

### PRESERVE8
specifies that the current file preserves 8-byte alignment of the stack

### THUMB
- Provides 16 Bit instruction set
- fetches instructions by 2 bytes

### ARM
- Provides 32 bit instruction set
- Fetches instructions by 4 bytes

### DCB (1 byte)
Allocates one or more bytes of memory, and defines the initial runtime contents of the memory

### DCD (4 bytes)
Allocates one or more words of memory, aligned on 4-byte boundaries, and defines the initial runtime contents of the memory.

### DCW (2 bytes)
Allocates one or more halfwords of memory, aligned on 2-byte boundaries, and defines the initial runtime contents of the memory


### SPACE (1 byte)
```
store_table             SPACE   16 ; reserves 16 byte
```

## AREA Instruction

The AREA directive instructs the assembler to assemble a new code or data area. Areas are independent, named, indivisible chunks of code or data that are manipulated by the linker. 

```assembler
    AREA name{,attr}{,attr}...
```

![Arm Reference](https://developer.arm.com/documentation/dui0041/c/Assembler/Directives/AREA-directive)

### Code

```assembler
    AREA myCode, CODE, READONLY
```

### Variables

```assembler
    AREA myAsmVar, DATA, READWRITE

    ; VARIABLES

    ALIGN
```

