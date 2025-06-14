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
vir_addr_space = 32  # in bits 
page_size = 1e3      # in bytes

# phy_memory_size != n_phy_addr_lines 
# if n_phy_addr_lines is given -> phy_memory_size = (2^n_phy_addr_lines)   
phy_memory_size = 2**24  # in bytes 

n_pages, vpn_size, vpo_size, n_phy_addr_lines, ppn_size, ppo_size \
    = n_page_entries(vir_addr_space, page_size, phy_memory_size)

print(f'Physical Memory Size: {phy_memory_size} Bytes results in Physical Address Space: {n_phy_addr_lines}')
print(f'PPN Size: {ppn_size}-Bits & PPO Size: {ppo_size}-bit\n')

print(f'Virtual Address Space: {vir_addr_space} with a Page Size of {page_size} results in:')
print(f'n Pages: {n_pages} & VPN Size: {vpn_size}-Bits & VPO Size: {vpo_size}-bit')