# Memory

## Cache

- fast memory close to, or integrated with, the processor
- transparent to the programmer
- When the code accesses a variable the cache controller checks whether the contents of the address is in cache memory
	- If yes -> cache hit
	- If no -> cache miss -> processor accesses the address in memory and reads a line/block
		- whilst being read by processor, the line read is also put into the cache memory

## Paging

- An address space is divided into pages (typically 4k, now -> 2M)
- A physical memory is divided into frames of the same size
- When code is required or a memory access happens the entire page is fetched into memory from the hard-disk

- Due to relative addressing, the page can be placed in any frame in memory
- Thus only the pages the code is actually using need to be in main memory
- Efficient use of main memory
	- Support for multiprocessing


TODO