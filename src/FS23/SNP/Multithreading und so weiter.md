## Multi-Tasking

**Task**: Eine Aufgabe die von der CPU abgearbeitet wird
**Batch-Ausführen**: Führ die anstehenden Tasks **nacheinander** durch.
**Multi-Tasking**: Führt die Prozesse **gleichzeitig / nebeneinander** aus


### Scheduling

**Kooperativ**: Jeder Task entschieden, wann sie die Kontrolle an einen anderen Task abgibt.
**Präemptiv**: Kontrollübergabe an den nächsten Task wird erzwungen
**Scheduler**
- Unterbricht präemtiv
- entscheidet welche Tasks dran sind
	- Round robin (im Kreis herum)
	- Priority driven


# Fork
Nach dem fork existiert der Kindprozess als Kopie des original Prozesses.
- Bisherige Variablen werden also exakt kopiert
- Somit sind auch offene Files dann „doppelt“ vorhanden. Also immer aufpassen
```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

#define PERROR_AND_EXIT(M) do { perror(M); exit(EXIT_FAILURE); } while(0)

int main()
{

	// Erstelle neuen Child prozess
	// setzt DANACH die childId
	pid_t childId = fork();
	if (childId == -1)
	{
	  PERROR_AND_EXIT("fork");
	}
  
	if (childId > 0)
	{
		// ChildId ist gesetzt, also sind wir im Parent
		printf("Parent: %d forked child %d\n", getpid(), cpid);
	
		int wstatus;

		// Jetzt warten wir, bis der Prozess des Kindes
		// fertig ist, 0 -> kein timeout also unendlich lange
		pid_t wpid = waitpid(cpid, &wstatus, 0);
		printf("Child exited with status: %d \n", WEXITSTATUS(wstatus));

		// jetzt beenden wir den Parent mit Success
		exit(EXIT_SUCCESS);
	}
	else
	{
		// Da childId noch nicht gesetzt ist, zum Zeitpunkt des forks
		// Wissen wir, dass wir im child sind


		printf("Child: %d forked by parent %d\n", getpid(), getppid());
		sleep(3);
		exit(123);
	}
}

// Parent erstellt neues Kind
// Kind wird ausgeführt, blockiert parent bis abgeschlossen (exit)
// Parent wird abgeschlossen (exit)
```


# Exec
Ersetzt den Childprozess durch ein anders ausführbares Programm.
```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

#define PERROR_AND_EXIT(M) do { perror(M); exit(EXIT_FAILURE); } while(0)

int main()
{
	// Erstelle neuen Child prozess
	// setzt DANACH die childId
	pid_t childId = fork(); // Erstelle neues Kind
	if (childId == -1)
	{
		PERROR_AND_EXIT("fork");
	}
	
	if (childId > 0)
	{
		// ChildId ist gesetzt, also sind wir im Parent
		printf("Parent: %d forked child %d\n", getpid(), cpid);
	
		int wstatus;

		// Jetzt warten wir, bis der Prozess des Kindes
		// fertig ist, 0 -> kein timeout also unendlich lange
		pid_t wpid = waitpid(cpid, &wstatus, 0);
		printf("Child exited with status: %d \n", WEXITSTATUS(wstatus));

		// jetzt beenden wir den Parent mit Success
		exit(EXIT_SUCCESS);
	}
	else
	{
		// Da childId noch nicht gesetzt ist, zum Zeitpunkt des forks
		// Wissen wir, dass wir im child sind


		// Wir definieren die Befehle einzel
		// in diesem fall „ls -l“
		static char *eargv[] = { "ls", "-l", NULL };
		
		if (execv("/bin/ls", eargv) == -1)
		{
			PERROR_AND_EXIT("execv: /bin/ls")
		}

		// Das exec denn Prozess ersetzt, wird diese Zeile nie getroffen
	}
}
```

# System
1. Spaltet einen Prozess ab **fork())**
2. startet die System-Shell, führt in dieser Shell das angegebene Kommando aus
3. Wartet blockierend auf das Terminieren des Prozesses (waitpid())

### WEXITSTATUS
Extrahiert den Exitcode aus dem zurückgegebenen Status des system() Befehles

```c
int ret = system("/bin/ls -l");
```

# POPEN
![[Pasted image 20230527193800.png]]

# Threads

Da das OS die Threads selber verwaltet, kann es sein, dass die Ausgabe auf der Konsole sich verändert. Wenn jetzt z.B. der Child Prozess eine höhere Priorität hat, dann ist es möglich, dass dieser **VOR** dem Main prozess endet.

```c
#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <unistd.h>
#include <pthread.h>

#define PERROR_AND_EXIT(M) do { perror(M); exit(EXIT_FAILURE); } while(0)

// Definiere den worker thread, diese Funktion
// wird im thread später ausgeführt
void *worker(void *arg)
{
	printf("worker\n");
	sleep(3);
	static int ret_value = 123;
	return &ret_value;
}

int main()
{
	pthread_t thread;

	// erstelle neuen thread
	// thread -> speichere diesen in die thread adresse
	// NULL -> pthread_attr_t: erlaubt also einige Attribute zu setzen
	// worker -> welche Funktion soll ausgefüht werden
	// NULL -> argument zur Funktion, da kann auch alles mögliche drin stehen
	
	int status = pthread_create(&thread, NULL, worker, NULL);
	if (status != 0)
	{
		// Thread konnte nicht erstellt werden
		exit (status);
	}

	printf("main\n");
	
	static void *retVal;
	status = pthread_join(thread, &retVal);
	if (status != 0)
	{
		// Thread konnte nicht beigetreten werden,
		// es ist etwas schief gelaufen
		exit (status);
	}

	printf("worker retval = %d\n", *((int*)retval));
	exit (EXIT_SUCCESS);
}

```

## Loslassen eines Threads (Detach)
**Funktion**: pthread_detach() 
Gibt an, dass sobald der Thread beendet wird, die Ressourcen freigegeben werden. Normalerweise passiert dies erst beim **pthread_join**. 

-> Es darf **NICHT** mit pthread_join auf den Prozess gewartet werden, da dieser bereits weg sein kann.

## Terminierung eines Threads

- **return**: Standardmässig, der Rückgabewert wird bei pthread_join zurückgegeben.
- **pthread_exit**: so ist es möglich, den thread zu beenden. Der Rückgabewert wird bei **pthread_join** gelesen.
- **exit** beendet den übergeordneten Prozess
- **pthread_cancel**: Wird verwendet um den Prozess zu beenden.

