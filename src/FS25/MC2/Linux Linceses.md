# Linux Licenses  

## GNU General Public License

General “Four Freedoms”:
0. The freedom to runthe program, for any purpose.
1. The freedom to studyhow the program works, and modifyit so it does your computing as you wish.
2. The freedom to redistributecopies so you can help your others.
3. The freedom to distribute copies of your modifiedversions to others.

Condition
- The source code needs to be available!

GNU is a recursive acronym: "GNU's Not Unix!"

- GPL a copyleft license:  
	→ Changes have to be released under the same license
- Programs linked with a library released under the GPL must also be released under the GPL

Linux Kernel sources are Free Software released under the GNU General Public License version 2 (GPLv2).  

=>

- When you receive or buy a device with Linux on it, you must  
	→ receive the Linux sources, with the   
	→ right to study, modify and redistribute them.  
- When you produce Linux based devices, you must   
	→ release the sources to the recipient, with the same rights, with no restriction.

## GPL Redistribution

Providing source code?
- If software isn't distributed -> no need to provide source code  
	=> Modification can be kept secret until delivery
- If software is distributed -> following options:
	- Release binary with   
		a) copy of the source on a physical medium  
		b) with the network address of a location pointing to source code   
		c) with a written offer valid for 3 years that indicates how to fetch the source code

If you don’t want to provide Source Code, compile with LGPL (Lesser GPL)

## Lesser General Public License

- LGPL also  a copyleft license:  
	→ Changes have to be released under the same license

Programs **linked against a library** under the LGPL **do not need to be released under the LGPL and can be kept proprietary**.

User must keep the ability to update the library independently from the program.  
→ Dynamic linking is the easiest solution.

## Tainted Kernel

**MODULE_LICENSE**: If this macro is not set to some sort of GPL license tag, then the kernel will become “tainted” when you load your module.

Tainted Status
- **G**: All modules loaded were licensed under the GPL or a license compatible with the GPL.
- **P**: The kernel has a proprietary license loaded. (Module or Kernel)

Decode tainted level on Bitlevel:
```bash
for i in $(seq 18); do echo $(($i-1)) $(($(cat /proc/sys/kernel/tainted)>>($i-1)&1));done
```

![alt text](media/tainted%20kernel%20bits-%20Kernel%20Module.png)

## Permissive Licenses

MIT and BSD:  
Common for both: “Permitted to do whatever the user wants without any
legal obligation to the owner.”
- Permits use
- Permits redistribution
- Permits redistribution with modification
- Provision to retain the copyright notice and warranty disclaimer
- Not required that source code is distributed
- Only requirement: Include a copy of the license

In addition, the MIT license also explicitly allows:
- merging
- publishing
- sublicensing
- selling

## Mozilla Public License

- Development of the Netscape Public License which was created with the publication of the Netscape source code in 1998.
- Copyleft license: It grants liberal copyright and patent licenses allowing for free use, modification, distribution, and exploitation of the work
- Modifications of MPL code must again be MPL

## Comparison of open licenses

[https://choosealicense.com/licenses/](https://choosealicense.com/licenses/)
