# Device Tree

## Purpose

- Informs the Linux about the hardware
- At which (physical) addresses memory blocks are found and their size
- The address where the registers of the peripherals are and the range
- Where the interrupts of the peripherals are connected to
- Where the GPIO or peripherals pins are connected to the outside
- What alternate functions must be selected to connect the peripheral
- Which driver has to be loaded for which peripheral
- Enabling the driver

## Mechanism

1. Device Tree is parsd
2. Compatible Driver in Kernel is searched and started
3. Driver gets additional properties from Device Tree


```dtb
{
	node@ {
		a-string-property = "A string";
		a-string-list-property = "first string", "second string";
		a-byte-data-property = [0x01 0x23 0x34 0x56]

		child-node@ {
			first-child-property;
			second-child-property = <1>;
			a-reference-to-something = <&node1>;
		};

		child-node@1 {
		};
	};

	node1: node@1 {
		an-empty-property;
		a-cell-property = <1 2 3 4>;
		child-node@0 {
		};
	};
};
```


## Is ARM or Legacy?

| Bit count | |
|-----------|-|
| 32 bit | legacy |
| 35 bit | arm |

```python,editable
def hex_to_bits(hex_num):
    # Convert the hex number to an integer
    decimal_num = int(hex_num, 16)
    
    # Convert the integer to binary and remove the "0b" prefix
    binary_num = bin(decimal_num)[2:]
    
    # Return the binary number (padded to 4 bits for each hex digit if needed)
    return binary_num.zfill(len(hex_num) * 4)

# Example usage
hex_num = "0x7e804000"
hex_num = hex_num.replace('0x', '')
binary_rep = hex_to_bits(hex_num)

print(f"Hex: {hex_num} -> Bits: {len(binary_rep)}")
if len(binary_rep) == 32:
	print ("LEGACY")
else:
	print ("ARM")
```