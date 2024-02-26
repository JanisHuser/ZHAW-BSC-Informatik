# Processes

- Unit of resource ownership
- Unit of scheduling
- POSIX defined

A process is a running program
- Process is a program in execution – has its own main()
- The process owns resources (memory, file handles ...)
- The process is assumed to have exclusive access to all computing and hardware resources 100% of the time
- The process may be managed by an operating system (OS)
- In a multi-process OS, the OS will schedule the process according to some policy
- The memory protection unit (HW) will protect the integrity of the process’ memory from other processes

## POSIX Processes (Portable Operating System Interface)

- Behavioural specification
- Defines how processes and threads are created and terminated
- Operating systems may (or may not) support POSIX

- Process creation through a *fork()*
- *fork()* clones <span style="text-decoration: underline">total copy</span> the calling process to child
- Child iherits copies of resources
	- Child/parent variables are handled sperately <span style="text-decoration: underline">copy on write</span>
- Parent and child run independently of each other - scheduled seperately by the OS
- OS specific effects
	- The child is in the process hierarchy of the parent
	- Parent normally responsible for cleaning up after child. A calling process (should) *wait()* for the child to end.

```c
#include <sys/types.h>
#include <stdio.h>

int main(void) {
	pid_t ret;
	ret = fork();		// make child
	if (ret == 0) {
		printf("I am the child\n");
		if (execl("./test", NULL) < 0) {
			// the following section should not be reached
			printf("could not exec");
			exit(-1);
		}
	} else {
		wait (NULL);
	}
}
```