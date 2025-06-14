# MMU




## Calculate Number of Page Entries

```python
def n_page_entries(vir_addr_space, page_size):
    # Determine virtual page offset (VPO) size 
    vpo_size = round(math.log(page_size, 2))
    
    # Determine virtual page number (VPN) size 
    vpn_size = vir_addr_space - vpo_size
    
    # Return number of possible page entries, vpn_size, vpo_ize
    return 2 ** vpn_size, vpn_size, vpo_size

# Example usage
vir_addr_space = 16 
page_size = 4000

n_pages, vpn_size, vpo_size = n_page_entries(vir_addr_space, page_size)
print(f'Virtual Address Space: {vir_addr_space} with a Page Size of {page_size} results in:')
print(f'n Pages: {n_pages} & VPN Size: {vpn_size}-Bits & VPO Size: {vpo_size}')
```