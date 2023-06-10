Sync / Semaphores und Signals werden verwendet um Zugriff auf geteilte Ressourcen zu koordinieren. Zudem können damit Threads aufeinander warten.

Syncs werden notwendig, wenn ein Thread auf einen anderen warten **muss**.
- z.B. wenn eine Resource im einten geöffnet ist, dann darf der andere diese erst öffnen, sobald der erste durch ist.
- Oder in einer kritischen Funktion, die **IMMER** ganz durchlaufen werden muss.

```c
// Mit dem volatile keyword wird klargestellt,
// dass diese Resource von mehreren Threads verwendet wird.
volatile int iAmShared = 0;
```

# Mutex - Mutual Exclusion
- Resourcen werden gegenseitig ausgeschlossen, ein Task blockiert den Eintritt für andere Tasks in die Crititcal Section

## Probleme
- Runtime Kosten (locks dauern)
- Rekursion
- Kein Unlock (Bei early return)
- Deadlock

```c
#include <sys/types.h>
#include <phtread.h>
#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>

const int N = 100000000;

// shared value
volatile int value = 0;

pthread_mutx_t mutex;

void * thread_method(void * arg)
{
	int delta = *(int*) arg;

	for (int i = 0; i < N; i++)
	{
		if (pthread_mutex_lock(&mutex) != 0)
		{
			perror("Mutex konnte nicht besetzt werden");
			exit(EXIT_FAILURE);
		}

		// Gemeinsame Variable auslesen
		int a = value;

		// Modifiziern
		a += delta;

		// Variable wieder setzen
		value = a;


		// Mutex wieder freigeben
		if (pthread_mutex_unlock(&mutex) != 0)
		{
			perror("Mutex konnte nicht freigegeben werden");
			exit(EXIT_FAILURE);
		}
	}
	return NULL;
}

int main (void)
{
	if (phtread_mutex_init(&mutex, NULL) != 0)
	{
		perror("Mutex konnte nicht initialisiert werden");
		exit(EXIT_FAILURE);
	}

	pthread_t th_inc;
	pthread_t th_dec;


	int inc = +1;
	int dec = -1;
	if (pthread_create(&th_inc, NULL, count, &inc) != 0)
	{
		perror("Thread konnte nicht erstellt werden");
		exit(EXIT_FAILURE);
	}
	
	if (pthread_create(&th_dec, NULL, count, &dec) != 0)
	{
		perror("Thread konnte nicht erstellt werden");
		exit(EXIT_FAILURE);
	}

	// noch auf threads waretn
	if (pthread_join(th_inc, NULL) != 0)
	{
		perror("Thread konnte nicht beendet werden");
		exit(EXIT_FAILURE);
	}
	if (pthread_join(th_dec, NULL) != 0)
	{
		perror("Thread konnte nicht beendet werden");
		exit(EXIT_FAILURE);
	}

}
```

# Semaphore
Tasks können über Semaphoren Synchronisationspunkte vereinbaren

## Probleme
- Synchronisation kostet Zeit
- Wenn ein wait zu viel, bzwh. ein signal zu wenig
- Deadlocks, System kann komplett blockiert werden

```c
// C program to demonstrate working of Semaphores
#include <stdio.h>
#include <pthread.h>
#include <semaphore.h>
#include <unistd.h>

sem_t mutex;

void* thread(void* arg)
{
	//wait
	sem_wait(&mutex);
	printf("\nEntered..\n");

	//critical section
	sleep(4);
	
	//signal
	printf("\nJust Exiting...\n");
	sem_post(&mutex);
}


int main()
{

	// 1 -> Initial value
	// unbedingt auf das achten
	sem_init(&mutex, 0, 1);
	pthread_t t1,t2;
	pthread_create(&t1,NULL,thread,NULL);
	sleep(2);
	pthread_create(&t2,NULL,thread,NULL);
	pthread_join(t1,NULL);
	pthread_join(t2,NULL);
	sem_destroy(&mutex);
	return 0;
}

```

