# Threads

- Under POSIX, created within a process
- Operates in the context of a process
- Can access all process resources including memory
- Kernel management threads - kernel knows threads exist and schedules them
	- default linux behaviour
- User threads - threading in user space
	- kernel does not know of their existence
	- user-threads library scheduler, not OS scheduler, schedules threads

```c
#include <pthread.h>
int aVar = 16;

void *PrintMessageFunction(void *ptr) {
	printf ("&s: %d\n", (char*)ptr, ++aVar);
}

int main (void) {
	pthread_t thread1, thread2;
	char *message1 = "Hello";
	char *message2 = "World";

	pthread_create(&thread1, NULL, PrintMessageFunction, (void*)message1);
	pthread_create(&thread2, NULL, PrintMessageFunction, (void*)message2);

	// wait for termination of thread 1, then thread 2
	pthread_join (thread1, NULL);
	pthread_join (thread2, NULL);

	printf("Hauptprogramm (Vater‐Thread) beendet \n");
	exit(0);
}
```