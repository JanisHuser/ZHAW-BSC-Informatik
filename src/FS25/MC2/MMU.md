# MMU

![alt text](media/principle%20-%20mmu.png)


![alt text](media/principle%202%20-%20mmu.png)

## Expanding Address Space (Historical)

![alt text](media/overlay%20tech%20-%20mmu.png)

![alt text](media/bank%20switching%20-%20mmu.png)

![alt text](media/bank%20switching%202%20-%20mmu.png)

## "Expanding" Physical memory

### MEMORY MANAGEMENT USING SEGMENTATION

See presentation pages 19-22.

### MEMORY MANAGEMENT BY PAGING

![alt text](media/principle%20paging%20-%20mmu.png)

![alt text](media/principle%20addr.%20translation%20-%20mmu.png)

For more detail on Paging see slides pages 27ff.

Loading the pages using the DMA - See page 50.

## Segmenting vs. Paging

|               | Paging | Segmentation |
|---------------|-------------|-------------|
| Advantages    | <ul><li>No Adder needed</li><li>Equal Page Size, easy Swapping</li><li>Transparent to programmer</li><li>Easy Memory management algorithm</li></ul> | <ul><li>Segment table use lesser memory than page table</li><li>Flexible segment size saved memory</li></ul> |
| Disadvantages | <ul><li>Longer Memory look up times</li><li>Page tables consume additional memory</li><li>Transparent to programmer</li><li>Because of fixed Page size not full memory</li></ul> | <ul><li>Unequal page size disadvantage for swapping</li><li>Demands Programmer intervention</li><li>Costly management algorithm</li><li>Adder/Comparator uses chip size</li></ul> |

## Cache and Translation Look Aside Buffer

See presentation pages 60-66.


## Calculate Number of Page Entries, VPN, VPO, PPN, PPO

```python
import math

def n_page_entries(vir_addr_space, page_size, phy_memory_size):
    # Determine virtual page offset (VPO) size 
    vpo_size = round(math.log(page_size, 2))
    
    # Determine virtual page number (VPN) size 
    vpn_size = vir_addr_space - vpo_size
    
    # Determine DRAM n_Address_Lines <=> physical address size
    # => also physical page number (PPN) & physical page offset (PPO)
    n_phy_addr_lines = round(math.log(phy_memory_size, 2))
    ppn_size = n_phy_addr_lines - vpo_size
    ppo_size = vpo_size

    # Return number of possible page entries, vpn_size, vpo_ize, n_phy_addr_lines
    return 2 ** vpn_size, vpn_size, vpo_size, n_phy_addr_lines, ppn_size, ppo_size

# Example usage
vir_addr_space = 16  # in bits 
page_size = 4000     # in byte

# phy_memory_size != n_phy_addr_lines 
# if n_phy_addr_lines is given -> phy_memory_size = (2^n_phy_addr_lines)   
phy_memory_size = 16e3 # in bytes 

n_pages, vpn_size, vpo_size, n_phy_addr_lines, ppn_size, ppo_size \
    = n_page_entries(vir_addr_space, page_size, phy_memory_size)

print(f'Physical Memory Size: {phy_memory_size} Bytes results in Physical Address Space: {n_phy_addr_lines}')
print(f'PPN Size: {ppn_size}-Bits & PPO Size: {ppo_size}-bit\n')

print(f'Virtual Address Space: {vir_addr_space} with a Page Size of {page_size} results in:')
print(f'n Pages: {n_pages} & VPN Size: {vpn_size}-Bits & VPO Size: {vpo_size}-bit')
```