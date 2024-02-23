# OS


- control resource usage, granting resource requestst, accounting for usage, mediate conflicting requests.

![alt text](<media/Bildschirmfoto 2024-02-23 um 08.34.26.png>)

## CPU - Central Processing Unit

- Fetch first instruction from memory into registers, decode it to determine its type and operands, execute it, and then fetch, decode and execute subsequent instructions.


## Hardware Review

![alt text](media/image-1.png)

### Hyperthreading / Parallel pipelines

- Innerhalb eines Intel Cores, werden mehrere Threads gleichzeitig ausgeführt.
- Optimierung der Aufgaben

![alt text](media/image.png)

### Caches

Der Cache ermöglicht einen deutlich schnelleren Zugriff auf Daten als im Memory, Speicher. Der Cache ist aber relativ teuer in der Produktion.

- a: quad-core chip with a shared L2 cache
- b: quad core chip with seperate L2 caches

![alt text](media/image-2.png)

## Memory

![alt text](media/image-3.png)

## Input Output

- Huge amount of I/O Devices, Hard Drives, Network Interfaces, Serial Board, Keyboard, Mouse, Graphics, Cameras, etc.
- Devices connected with CPU via a Bus System (SW) I/O Interfaces (SW) and I/O Controllers (HW)
- There are many different Bus Standars
	- PCI
	- PCIe
	- DMI
	- SATA
	- US


![alt text](media/image-4.png)

## Operating System Variants

- Mainframe Operating Systems
- Server Operating Systems
- Multiprocessor Operating Systems
- Personal Computer Operating Systems
- Handheld Computer Operating Systems
- Embedded Operating Systems
- Sensor Node Operating Systems
- Real-Time Operating Systems
- Smart Card Operating Systems

## Context switch

Der Zustand eines Prozesses wird durch die Inhalte der Register auf dem CPU bestimmt. 
- Der Dispatcher befüllt die Register in der CPU.
- Im Durchschnitt 6 Switches pro Sekunden


### File Reading 

- 11 Schritte
![alt text](media/image-5.png)


## TRAP / Software interrupt

Der einzige Weg, um von User Space in den Kernel Space zu gelangen